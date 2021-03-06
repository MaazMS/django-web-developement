from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(required= False)

    class Meta:
        model = Post
        fields = ('post',)
