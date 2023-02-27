from django import forms
from .models import studinfo

class user_form(forms.ModelForm):
    class Meta:
        model=studinfo
        fields='__all__'