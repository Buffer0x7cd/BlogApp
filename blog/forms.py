from django import forms
from .models import Post, Feedback, Comment

class PostForm(forms.ModelForm):
    '''Form class For new blog post '''
    class Meta:
        model = Post
        fields = ('title', 'text')

class FeedbackForm(forms.Form):
    '''Form class For feed  back form '''
    title =  forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text')

