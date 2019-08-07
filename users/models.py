from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)

	first_name = models.CharField(max_length=10)
	middle_name = models.CharField(max_length=10)
	last_name = models.CharField(max_length=10)
	identification_no = models.CharField(max_length=10)
	birthday = models.CharField(max_length=11)
	secret_question = models.CharField(max_length=22)
	def __str__(self):
		return self.user.username
