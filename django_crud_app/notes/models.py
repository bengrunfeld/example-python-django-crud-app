from django.db import models

class Note(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	first_published_date = models.DateTimeField('Date Published')
	last_update_date = models.DateTimeField('Last Update')

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.content