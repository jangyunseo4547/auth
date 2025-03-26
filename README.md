## auth 구조 
- 로그인 기능 
- user 
    - username
    - passward
    - name

- Post (유저가 작성하는 게시글) : 유저에 속함.
    - UniqueID
    - title
    - content 
    - user_id (ForeignKey) : 부모와 연결해줌

- => 1:N 관계 (한사람이 여러개의 게시글을 작성함.)

- Comment
    - UniqueID
    - content
    - user_id
    - post_id

- => 1:N 관계 (로그인 - 게시글 - 댓글 )

## 암호가 이루어 지는 구조
- 암호화 : 평문을 난수로 바꿈
    - hash함수 : sha1(암호로 유추가능) -> sha256(유추 불가)
    - salt  : sha로 생성된 숫자 + (랜덤 숫자) 붙이기


## 0. setting
- 프로젝트 이름 : auth
- 앱 이름 : accounts 작성
- 공통 html 설정 : 밖에 templates에 base.html 만들기 

## 1. User 로그인 modeling
- `확장 가능성을 열어두고 커스텀` : 커스텀하면 넣고 싶은 기능을 확장가능  
    - AbstractUser : 장고안에 이미 로그인 기본 모델 구현
```python
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
    #phone = models.CharField(max_length=100) 기본에서 추가하고 싶은 기능
```

- `settings.py`
- 장고 Usermodel과 내가 만든 Usermodel이 충돌하기 때문에 내 User를 써달라고 해야 함.
    - AUTH_USER_MODEL = 'accounts.User'

- `migrations 하기`

## 2. create (signup 회원가입)
- `프로젝트 urls.py` : 앱으로 경로 설정 
```python 
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
```

- `앱 내 urls.py 생성` : 로그인 경로 설정
```python
from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
]
```

`앱 내 forms.py 생성` : 장고 내에 UserCreationForm 불러옴.
```python
from .models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = '__all__'
# UserCreationForm : 장고가 만든 User대신 내가 만든 Userform을 사용
```

`앱 내 views.py` : 종이 보여주기
```python
from .forms import CustomUserCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        pass
    else:    # 1) get 요청 (내가 만든 Userform)
        form = CustomUserCreationForm()

    context = {
        'form':form,
    }
    return render(request, 'signup.html', context)
```
`signup.html` : base.html
```
{% extends 'base.html' %}

{% block body %}
    {{form}}
{% endblock %}
```

- `forms.py` : 필요없는 정보 빼고 네임, 비번만 남기기
```python 
fields= ('username',) # password는 필수라서 같이 나옴
```

- `views.py`
```python
def signup(request):
    if request.method == 'POST': #post일때 내가 커스텀한 form 불러오기
        form = CustomUserCreationForm(request.POST)
```

- `signup.html` : form의 method POST인 겨우/ 제출버튼 만들기 
```
{% extends 'base.html' %}

{% block body %}
    <form action="" method="POST">
        {% csrf_token %}
        {{form}}
        <input type="submit">
    </form>
{% endblock %}
```

## 3. create (로그인) 
### 로그인 기본 구조
- user -> myid, mypassward를 장고에게 전달 -> session 값을 create -> cookie에 저장
    - cookie : session값이 저장되어 있으면 로그인
    - expire_date: 짧을 수록 로그인 다시 해야 함. (보통 2주)

`앱 내 urls.py` : 로그인 경로 설정
```python
path('login/', views.login, name='login'),
```

`앱 내 forms.py` : form login 생성
```python
class CustomAuthenticationForm(AuthenticationForm):
    pass
```

`앱 내 views.py` : login 함수 만들기
```python
def login(request):
    if request.method == 'POST':  # session 정보 생성
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:login') # 게시글의 인덱스 페이지로


    else:   #로그인 get 요청 보여주기
        form = CustomAuthenticationForm()

    context = {
        'form':form,
    }
    
    return render(request, 'login.html', context)
```
