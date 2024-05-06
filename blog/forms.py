from .models import Comment
from django import forms

# inherits from built-in Django class, Meta class to specify which Fields to include
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment # imported from Comment model
        fields = ('body',)