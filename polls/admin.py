from django.contrib import admin
from .models import People,Document
# Register your models here.
class AdminTable(admin.ModelAdmin):
	people_id = "people_id"

admin.site.register(People)	
admin.site.register(Document,AdminTable)
	