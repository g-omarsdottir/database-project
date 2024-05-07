from django import forms
from .models import Comment


# inherits from built-in Django class, Meta class to specify which Fields to include
class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post 
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Comment # imported from Comment model
        fields = ('body',)
