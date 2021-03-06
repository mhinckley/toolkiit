from django import forms
from .models import Post, Name
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('to_field','do_field', 'person', 'source_url', 'summary')


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "username")


class NameForm(forms.ModelForm):

    class Meta:
        model = Name
        fields = ('first_name','last_name')
