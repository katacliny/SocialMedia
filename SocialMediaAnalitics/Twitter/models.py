from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
	tweeter_user = models.CharField(blank=True, null=True, max_length=300)
	text = models.TextField(blank=True, null=True)
	create = models.DateField(blank=True, null=True)
	hour = models.IntegerField(blank=True, null=True)
	locate = models.TextField(blank=True, null=True)
	num_word = models.IntegerField(blank=True, null=True)
	num_letter = models.IntegerField(blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.get(username="MasterBigData").pk)
	tag = models.TextField(blank=True, null=True, default="#Python")

	def __str__(self):
		return self.tweeter_user + str(self.create)
