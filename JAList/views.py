from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def mypage(request):
	return render(request,'comment.html')
	#return render(request, 'comment.html',{'newaudience':request.post['audiencename'],}) 

'''
#kay sir 04-13-2021
 
from CTList.models import Item

def Mainpage(request):

	if request.method == 'POST':
		newItem = request.POST['personEntry']
		Item.objects.create(text=newItem)
	else:
		newItem = ''

	return render(request,'comment.html',{'newPerson':newItem})	

	#item1=Item()
	#item1.text=request.POST.get('personEntry', '')
	#item.save()
	#return render(request, 'comment.html',{'newaudience':request.POST['audiencename'],}) 
	#return render(request, 'comment.html'{'newaudience': item1.text, 'newPlace':item2.text, })
	


#def mypage(request):
	#return render(request, 'comment.html',{'newaudience':request.post['audiencename'],}) 

'''


#	return render(request,'comment.html')
'''
	if request.method == 'post':
		return HttpResponse(request.post['audiencename'])
	return render(request,'comment.html')
'''
	
'''
def mypage(request):
	return render(request, 'sample.html',{''})
'''	

	#return HttpResponse('homepage')

'''
def homepage(request):
	#return HttpResponse('homepage')
	return render(request,'sample.html')

'''
