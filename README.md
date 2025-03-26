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

## 0. setting
- 프로젝트 이름 : auth
- 앱 이름 : accounts 작성
- 공통 html 설정 : 밖에 templates에 base.html 만들기 

## 1. User 로그인 modeling
- `확장 가능성을 열어두고 커스텀` 
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

## 2. 