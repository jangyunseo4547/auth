from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login # 내가 만든 함수 login과 중복되므로 장고 login의 이름을 바꿈.

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 유효한 값은 저장 / 잘못된 값은 사라짐
            form.save()
            return redirect('accounts:login') 

    else:    # 1) get 요청 (내가 만든 Userform 보여주기)
        form = CustomUserCreationForm()

    context = {
        'form':form,
    }
    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':  # session 정보 생성
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index') # 게시글의 인덱스 페이지로


    else:   #로그인 get 요청 보여주기
        form = CustomAuthenticationForm()

    context = {
        'form':form,
    }
    
    return render(request, 'login.html', context)