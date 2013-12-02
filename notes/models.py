from django.db import models

class Note(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	first_published_date = models.DateTimeField(auto_now=True)
	last_update_date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		"""Returns a pretty output when someone calls Note.objects.all()"""
		return self.title