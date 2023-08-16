from django import forms
from .models import Reviews


class CommentsForm(forms.ModelForm):
    # Adding a comment
    class Meta:
        model = Reviews
        fields = (
            'name', 'text', 'email'
        )