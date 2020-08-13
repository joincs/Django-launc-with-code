from django import forms
from .models import Join

class EmailForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ['email']
    
    