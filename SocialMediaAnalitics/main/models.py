from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserConfig(models.Model):
	consumer_key = models.TextField(default='km2MppUbx5dhTXYEF0WNmGRyT')
	consumer_secret = models.TextField(default='KqpgTK4O1UliFhpOSMrdCRRvWJlSoYarbNYXx51cbay3Qqrr7n')
	access_token = models.TextField(default='1071105441952923648-kZ4PzWqL1qhT8nWZWI3h6zHvPd0cD8')
	access_token_secret = models.TextField(default='MwOrSDreqI6qZiPnpqj8pDd30cqbtRkp6cJIaBR9zd8hh')
	filter_key = models.TextField(default="#Python")
	is_search = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.get(username="MasterBigData").pk)
	
	def __str__(self):
		return self.filter_key