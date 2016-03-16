from django.db import models

# Create your models here.
class People(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class Document(models.Model):

	people_id = models.ForeignKey(People)
	edication = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s %s" % (self.people_id,self.edication)

	def __str__(self):
		return "%s %s" % (self.people_id,self.edication)
		

		