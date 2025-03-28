from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required # create 함수 꾸며줌

# Create your views here.
def index(request):
    articles = Article.objects.all() # 1) 전체 게시글 불러오기
    context = {                      # 2) 전체 게시글 담아서 렌더
        'articles':articles,
    }
    return render(request, 'index.html', context)

@login_required #create 실행하기 전에 login_required부터 실행 
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) # title, content
        if form.is_valid():
            article = form.save(commit=False) # 임시 저장
            article.user = request.user # 로그인한 유저 정보
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    
    context = {
        'form':form,
    }
    return render(request, 'create.html', context)