from django import forms
from .models import UserConfig
class UpdateUserConfigForm(forms.ModelForm):
	class Meta:
		model = UserConfig
		fields = ["consumer_key", "consumer_secret", "access_token", "access_token_secret", "filter_key", "is_search"] 