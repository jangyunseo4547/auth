from django.forms import ModelForm
from .models import Article,Comment

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        # fields = '__all__'
        # fields = ('title', 'content', ) # user 정보만 빼고 보여줌.
        exclude = ('user',)

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        exclude = ('user', 'article',) 
        #fields = ('content',)