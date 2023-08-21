from django import forms
from .models import *


class CommentsForm(forms.ModelForm):
    # Adding a comment
    class Meta:
        model = Reviews
        fields = (
            'name', 'text', 'email'
        )


class RatingForm(forms.ModelForm):
    # Form for adding a rating
    star = forms.ModelChoiceField(
        queryset=RatingsStar.objects.all(), widget=forms.RadioSelect(),
        empty_label=None
    )

    class Meta:
        model = Reting
        fields = ('star',)