from django import forms
from .models import UserConfig
class UpdateUserConfigForm(forms.ModelForm):
	class Meta:
		model = UserConfig
		fields = ["consumer_key", "consumer_secret", "access_token", "access_token_secret", "filter_key", "is_search"] 
		widgets = {
            'consumer_key': forms.TextInput(attrs={'class': 'form-control'}),
            'consumer_secret': forms.TextInput(attrs={'class': 'form-control'}),
            'access_token': forms.TextInput(attrs={'class': 'form-control'}),
            'access_token_secret': forms.TextInput(attrs={'class': 'form-control'}),
            'filter_key': forms.TextInput(attrs={'class': 'form-control'}),
            'is_search': forms.TextInput(attrs={'class': 'form-control'}),
        }