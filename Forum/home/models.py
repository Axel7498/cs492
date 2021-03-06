from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	photo = models.FileField(blank=True, upload_to='posts')
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	time_now = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title


class Comment(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	body = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.user.username