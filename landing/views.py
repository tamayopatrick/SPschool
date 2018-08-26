from django.shortcuts import render
from django.http      import HttpResponse
from django.template  import loader
# Create your views here.

def land0(request):
	#return HttpResponse("Hello world! Im your ticher of spanich")
	template=loader.get_template("landing/landing.html")
	return HttpResponse(template.render())