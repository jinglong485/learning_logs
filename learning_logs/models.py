from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	"""A topic the user is learning about."""
	text = models.CharField(max_length=20)
	data_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a string representation of the model"""
		return self.text
	
class Entry(models.Model):
	"""Something specific learned about the topic"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "entries"

	def __str__(self):
		"""Return a simple representation of the entry"""
		return f"{self.text[:50]}..."