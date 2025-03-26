from .models import User # 1) 내가 만든 모델 불러오기
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm): #회원가입 정보 : id, 비번
    class Meta():
        model = User
        #fields = '__all__'
        fields= ('username',) # password는 필수라서 같이 나옴

class CustomAuthenticationForm(AuthenticationForm):
    pass


