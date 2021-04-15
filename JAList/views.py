#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
'''
def homepage(request):
	#return HttpResponse('homepage')
	return render(request,'sample.html')

'''


def mainpage(request):
	#return HttpResponse('homepage')
	return render(request,'sample.html')