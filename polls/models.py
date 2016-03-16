from django.db import models

# Create your models here.
class TableName(models.Model):
	
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class TableDocument(models.Model):

	people_id = models.ForeignKey(TableName)
	edication = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s %s" % (people_id,edication)

		