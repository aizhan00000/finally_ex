from django import forms
from .models import Enrollment


class SignupCreateForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['first_name', 'last_name', 'pr_language', 'title']