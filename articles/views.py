from django.shortcuts import render,redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
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

def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()    # detail 페이지에 댓글
    context = {
        'article':article,
        'form':form,
    }
    return render(request, 'detail.html', context)

@login_required
def update(request,id):
    article = Article.objects.get(id=id)

    if request.user != article.user:  # 게시글 작성한 사람만 수정 가능
        return redirect('articles:index')

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=id)
    else:
        form = ArticleForm(instance=article) # article 가져오기
    
    context= {
        'form':form,
    }
    return render(request, 'update.html',context)

@login_required
def delete(request,id):
    article = Article.objects.get(id=id)
    if request.user == article.user:
        article.delete()

    return redirect('articles:index')

@login_required
def comment_create(request, article_id):
    form = CommentForm(request.POST)  # get 요청으로 들어오는 경우가 없기 때문에

    if form.is_valid():
        comment = form.save(commit=False)

        # 1) 객체를 저장하는 경우
        # comment.user = request.user # 유저찾기
        # article = Article.objects.get(id=article_id) # 게시글 
        # comment.article = article

        # 2) id 값을 저장하는 경우
        comment.user_id = request.user.id   # db는 user_id를 저장하기 때문에 지원해줌.
        comment.article_id = article_id

        comment.save()

        return redirect('articles:detail', id=article_id)

@login_required
def comment_delete(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.user:
        comment.delete()
    
    return redirect('articles:detail', id=article_id)        