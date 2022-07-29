from difflib import context_diff
import imp
from statistics import variance
from django.shortcuts import render,HttpResponse
from matplotlib.style import context
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
	context={
		'var':"this is sent"
	}
	messages.success(request,'This is a test message')
	return render(request,'index.html',context)
def about(request):
	return render(request,'about.html')
def contact(request):
	if request.method == "POST":
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Phone=request.POST.get('Phone')
		contact=Contact(Name=Name,Email=Email,Phone=Phone,desc="vnvgnrg",date=datetime.today())
		contact.save()
		messages.success(request, 'Your details are upadted')
	return render(request,'contact.html')
def services(request):
	return render(render,'services.html')
