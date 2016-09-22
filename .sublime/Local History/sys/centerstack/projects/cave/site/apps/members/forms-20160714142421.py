#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Member ModalForm
#*============================ #
from django import forms
from .models import Member
from .models import Level
from .models import ReferralSource
from .models import Expertise
from .models import Certification



class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = '__all__'


class LevelForm(forms.ModelForm):
	class Meta:
		model = Level
		fields = '__all__'


class ReferralSourceForm(forms.ModelForm):
	class Meta:
		model = ReferralSource
		fields = '__all__'


class CertificationForm(forms.ModelForm):
	class Meta:
		model = Certification
		fields = '__all__'


class ExpertiseForm(forms.ModelForm):
	class Meta:
		model = Expertise
		fields = '__all__'






