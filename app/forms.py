from django import forms
from django.contrib.auth.models import User
from .models import Movies, Category
from django.contrib.auth.forms import UserChangeForm


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['movie', 'slug', 'description', 'release_date', 'image', 'cast', 'imdb_rating', 'trailer_link',
                  'category',
                  'comments_or_review', ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category"]


class UserProfileForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')
