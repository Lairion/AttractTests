# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from polls.models import Document,People

class Command(BaseCommand):
	help = u"For this command, you need to enter 3 argument.\
	\nThe first argument must contain a selection condition used for search.\
	\n The second argument is responsible for the field type in which the search will take place. The argument must choose from the following options:\n \
	\n  --id_srch\
	\n  --education_srch\
	\n  --name_srch\
	\n The third argument is responsible for the return of the result on the selection condition. The argument must choose from the following options:\n \
	\n  --id\
	\n  --education\
	\n  --name"



	def add_arguments(self,parser):
		
		parser.add_argument('condition', nargs = '+',type=str)

		
		parser.add_argument('--id',
            action='store_true',
            dest='id',
            default=False,
            help=u'Return id field')
		
		parser.add_argument('--education',
            action='store_true',
            dest='education',
            default=False,
            help=u'Return education field')
		
		parser.add_argument('--name',
            action='store_true',
            dest='name',
            default=False,
            help=u'Return name field')
		
		parser.add_argument('--id_srch',
            action='store_true',
            dest='id_srch',
            default=False,
            help=u'Search in id field')
		
		parser.add_argument('--education_srch',
            action='store_true',
            dest='education_srch',
            default=False,
            help=u'Search in education field')
		
		parser.add_argument('--name_srch',
            action='store_true',
            dest='name_srch',
            default=False,
            help=u'Search in name field')

	def search_in_name(self,condition,type_area):
		for obj in People.objects.all():
					if condition == obj.name:
						filt = Document.objects.filter(people_id=obj.id).values_list(type_area,flat=True)
						for result in filt:
							self.stdout.write("%s\n" % (result), ending='')
						self.stdout.write("\n", ending='') 
	
	def filt_in_edication(self,condition,type_area):
		result = Document.objects.filter(education=condition).values_list(type_area,flat=True)
		return result
	
	def filt_in_id(self,condition,type_area):
		result = Document.objects.filter(id=condition).values_list(type_area,flat=True)
		return result
	
	def handle(self,*args,**options):
		condition = " ".join(options['condition'])
		people_all = People.objects.all()
		document_all = Document.objects.all()
		self.stdout.write(u" %s \n" % (condition), ending='')
		self.stdout.write("=============================================\n", ending='')
		if (options['education'] and (options['name_srch'] or options['id_srch'])):
			if options['name_srch']:
				self.search_in_name(condition,'education')
				
			elif options['id_srch']:
				condition = int(condition)
				result = self.filt_in_id(condition,'education')
				self.stdout.write("%s" % "".join(result), ending='')

		elif (options['name'] and (options['education_srch'] or options['id_srch'])):
			if options['education_srch']:
				fk = self.filt_in_edication(condition,'people_id')
				for name_id in fk:
					name = str(People.objects.get(pk=name_id))
					self.stdout.write("%s\n" % (name), ending='')
			if options['id_srch']:
				condition = int(condition)
				fk = self.filt_in_id(condition,'people_id') 
				for name_id in fk:
					name = str(People.objects.get(pk=name_id))
					self.stdout.write("%s\n" % (name), ending='')	

		elif (options['id'] and (options['education_srch'] or options['name_srch'])):
			if options['education_srch']:
				array = self.filt_in_edication(condition,'id')
				for result in array:
					self.stdout.write("%s\n" % (result), ending='')
			if options['name_srch']:
				self.search_in_name(condition,'id')

		self.stdout.write("=========================", ending='')
		self.stdout.write("Document table All", ending='')
		self.stdout.write("=========================\n", ending='')
		for people in document_all:
			self.stdout.write("%s \n" % (people), ending='')		
		

			
		

	
