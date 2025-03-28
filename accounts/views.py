from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login # 내가 만든 함수 login과 중복되므로 장고 login의 이름을 바꿈.
from django.contrib.auth import logout as auth_logout 
from .models import User

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 유효한 값만 저장 / 유효하지 않다면 저장x
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':  # session 정보 생성
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            
            # /accounts/login/ => create로
            # /accounts/login/?next=/articles/create/ => 로그인 안하고 게시글 작성하려 할때
            next_url = request.GET.get('next')

            # next가 없을때 => None or 'articles:index'(o)
            # next가 있을때 => 'articles/create'(o) or 'articles/index'
            return redirect(next_url or 'articles:index') # 게시글의 인덱스 페이지로


    else:   #로그인 get 요청 보여주기
        form = CustomAuthenticationForm()

    context = {
        'form':form,
    }
    
    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def profile(request, username):
    user_profile = User.objects.get(username=username) # username을 기반으로 찾기 (user는 중복되지 않기 때문에)

    context = {
        'user_profile':user_profile,     # 내가 쓰는 유저 이름 바꿔주기 (장고 유저와 충돌 방지)
    }
    return render(request, 'profile.html', context)