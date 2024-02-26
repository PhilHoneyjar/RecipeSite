from django import forms
from .models import Recipe, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'prep_time', 'image', 'categories']


class RecipeCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass
