#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 main/views.py
#*====================== #
import os
import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.template import RequestContext
from preferences.models import Preference
from preferences.forms import PreferenceForm
from members.models import Level
from members.models import ReferralSource
from members.models import Expertise
from members.models import Certification
from members.forms import LevelForm
from members.forms import ReferralSourceForm
from members.forms import ExpertiseForm
from members.forms import CertificationForm
from datetime import datetime
import braintree



#	Main View
# ========================= #
def main(request, template):
	context = {}
	return render(request, template, context)




#	Admin
# ====================================== #
@login_required
def admin(request):
	context = {}
	return render(request, context)






#	Dropdown - Level - New
# ========================= #
def dropdowns(request, template):
	levels = Level.objects.all()
	form = LevelForm()
	context = {
		"levels": levels,
		"LevelForm": form,
	}
	return render(request, template, context )



#	Dropdown - Level - New
# ========================= #
def dropdown_level_new(request, template):
	levels = Level.objects.all()
	if request.method == "POST":
		form = LevelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/dropdowns/')
	else:
		form = LevelForm()
	return render(request, template, {"levels":levels, "LevelForm": form } )



#	Dropdown - Level - Delete
# ========================= #
value = []
def dropdown_level_delete(request, template):
	if request.method == "POST":
		name = list(request.POST.getlist('checked'))
		logging.debug(name)
		for ii in name:
			Level.objects.get(pk=ii).delete()
		del name[:]
		return redirect('/dropdowns/')
	return render(request, template)






