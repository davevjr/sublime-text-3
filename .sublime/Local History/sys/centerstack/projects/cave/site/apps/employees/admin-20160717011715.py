#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	member/admin.py
#*========================== #
from django.contrib import admin
from .models import Member
from .models import Level
from .models import ReferralSource
from .models import Expertise
from import_export import resources
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import DateWidget

class MemberResource(resources.ModelResource):
	dob = fields.Field(column_name='dob', widget=DateWidget)
	class Meta:
		model = Member



class MemberAdmin(ImportExportModelAdmin):
	list_display  = [f.name for f in Member._meta.fields]
	resource_class = MemberResource
	import_id_fields=['member_id']



admin.site.register(Member, MemberAdmin)
admin.site.register(ReferralSource)
admin.site.register(Level)
admin.site.register(Expertise)

