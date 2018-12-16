from django import forms
from .models import UserConfig
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
from .models import UserConfig as uc

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

    def __init__(self, *args, **kwargs):
        super(UpdateUserConfigForm, self ).__init__(*args, **kwargs)
        self.fields['consumer_key'].widget.attrs['readonly'] = uc.objects.filter(user = get_current_user()).first().is_search
        self.fields['consumer_secret'].widget.attrs['readonly'] = uc.objects.filter(user = get_current_user()).first().is_search
        self.fields['access_token'].widget.attrs['readonly'] = uc.objects.filter(user = get_current_user()).first().is_search
        self.fields['access_token_secret'].widget.attrs['readonly'] = uc.objects.filter(user = get_current_user()).first().is_search
        self.fields['filter_key'].widget.attrs['readonly'] = uc.objects.filter(user = get_current_user()).first().is_search
        self.fields['is_search'].widget.attrs['readonly'] = uc.objects.filter(user = get_current_user()).first().is_search

	