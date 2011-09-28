from django.db import models
from django.contrib.auth.models import User


class Comic(models.Model):
	"""
	This Model representation of a Comic
	"""
	
	title = models.CharField(max_length=50)
	date_published = models.DateTimeField()
	slug = models.SlugField(max_length=50)
	comic = models.ImageField(upload_to='comics')
	author = models.ForeignKey(User)

	def __unicode__(self):
		return "%s by %s" % (self.title, self.author.username)

	class Meta:
		verbose_name_plural = "Comics"

