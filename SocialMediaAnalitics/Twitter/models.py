from django.db import models

# Create your models here.

class Tweet(models.Model):
	tweeter_user = models.CharField(max_length=300)
	text = models.TextField()
	create = models.DateField()
	locate = models.TextField()
	num_word = models.IntegerField()
	num_letter = models.IntegerField()

	def __str__(self):
		return self.tweeter_user + str(self.create)


class UserConfig(models.Model):
	consumer_key = models.TextField(default='km2MppUbx5dhTXYEF0WNmGRyT')
	consumer_secret = models.TextField(default='KqpgTK4O1UliFhpOSMrdCRRvWJlSoYarbNYXx51cbay3Qqrr7n')
	access_token = models.TextField(default='1071105441952923648-kZ4PzWqL1qhT8nWZWI3h6zHvPd0cD8')
	access_token_secret = models.TextField(default='MwOrSDreqI6qZiPnpqj8pDd30cqbtRkp6cJIaBR9zd8hh')
	filter_key = models.TextField(default="#Python")
	is_search = models.BooleanField(default=False)

	def __str__(self):
		return self.filter_key