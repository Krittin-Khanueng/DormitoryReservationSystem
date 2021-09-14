from django.urls import reverse
from django.db import models


# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_time = models.DateTimeField(auto_now_add=True)
	last_updated_time = models.DateTimeField(auto_now=True)
	is_deleted = models.BooleanField(default=False)

	def __str__(self):
		return "<Blog: %s>" % self.title

	class Meta:
		ordering = ['-created_time']

	def get_url(self):
		return reverse('blog_detail', args=[self.pk])
