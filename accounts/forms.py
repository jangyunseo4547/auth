from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        #fields = '__all__'
        fields= ('username',) # password는 필수라서 같이 나옴

class CustomAuthenticationForm(AuthenticationForm):
    pass


