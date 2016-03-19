from django.core.management.base import BaseCommand
from polls.models import Document

class Command(BaseCommand):
	help = 'This help'

	def add_arguments(self,parser):
		parser.add_argument('condition',nargs='+',type=str)
		#parser.add_argument('area_condition',nargs='+',type=str)
		parser.add_argument('--id',
            action='store_true',
            dest='id',
            default=False,
            help='Search in id area.')
		parser.add_argument('--ediaction',
            action='store_true',
            dest='edication',
            default=False,
            help='Search in ediaction area.')
		parser.add_argument('--people_id',
            action='store_true',
            dest='people_id',
            default=False,
            help='Search in people_id area.')



	def handler(self,*args,**options):
		obj = Document.objects.all()
		if option['people_id']:
			self.stdout.write(obj.filter(edication=condition).order_by('people_id'))
		else:
			print hello

	
