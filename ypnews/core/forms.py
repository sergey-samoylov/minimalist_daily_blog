from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full mt-2 mb-2 p-2 border border-stone-400 bg-stone-400 text-stone-900'}),
            'password': forms.TextInput(attrs={
                'class': 'w-full mt-2 mb-2 p-2 border border-stone-400 bg-stone-400 text-stone-900'}),
            'password1': forms.TextInput(attrs={
                'class': 'w-full mt-2 mb-2 p-2 border border-stone-400 bg-stone-400 text-stone-900'}),
            'password2': forms.Textarea(attrs={
                'class': 'w-full mt-2 mb-2 p-2 border border-stone-400 bg-stone-400 text-stone-900'}),
        }
