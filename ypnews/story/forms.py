from django import forms
from django.forms import ModelForm

from .models import Comment, Story


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'w-full mt-2 mb-2 p-2 border border-stone-400 bg-stone-700 text-stone-400'}),
        }


class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = (
            'title',
            'url',
            'text',)

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full mt-2 mb-2 p-2 border border-stone-400 bg-stone-400 text-stone-900'}),
            'url': forms.TextInput(attrs={
                'class': 'w-full mt-2 mb-2 p-2 border border-stone-400 bg-stone-400 text-stone-900'}),
            'text': forms.Textarea(attrs={
                'class': 'w-full mt-2 mb-2 p-2 border border-stone-400 bg-stone-400 text-stone-900'}),
        }
