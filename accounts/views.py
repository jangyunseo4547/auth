from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 유효한 값은 저장 / 잘못된 값은 사라짐
            form.save()
            return redirect('accounts:login') 

    else:    # 1) get 요청 (내가 만든 Userform)
        form = CustomUserCreationForm()

    context = {
        'form':form,
    }
    return render(request, 'signup.html', context)