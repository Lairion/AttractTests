from django.contrib import admin
from .models import TableName,TableDocument
# Register your models here.
class AdminTable(admin.ModelAdmin):
	edication = "edication"

admin.site.register(TableName,AdminTable)	

	