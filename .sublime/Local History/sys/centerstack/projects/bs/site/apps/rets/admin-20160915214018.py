#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	interface/admin.py
#*========================== #
from django.contrib import admin
from .models import Property



#	Property
# ====================================== #
class PropertyAdmin(admin.ModelAdmin):
	list_display  		= [f.name for f in Property._meta.fields]
	ordering 			= ("id",)
admin.site.register(Property, PropertyAdmin)







