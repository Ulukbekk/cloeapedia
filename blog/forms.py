from django import forms

from blog.models import Post, Coment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'post', 'image')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'post', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ('name', 'text')


