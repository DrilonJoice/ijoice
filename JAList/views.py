from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def mypage(request):
	#return render(request, 'comment.html',{'newPerson':request.post}('comment_author'))
	return render(request,'comment.html',
		{'new_author':request.POST.get('comment_author',''),
		'new_email':request.POST.get('email',''),
		'new_comment':request.POST.get('comment',''),})
		
#kay sir 04-13-2021
 
#from CTList.models import Item

#def Mainpage(request):

	#if request.method == 'POST':
		#newItem = request.POST['personEntry']
		#Item.objects.create(text=newItem)
	#else:
		#newItem = ''
	#return render(request,'comment.html',{'newPerson':newItem})	



	#item1=Item()
	#item1.text=request.POST.get('personEntry', '')
	#item.save()
	#return render(request, 'comment.html',{'newaudience':request.POST['audiencename'],}) 
	#return render(request, 'comment.html'{'newaudience': item1.text, 'newPlace':item2.text, })

'''
'''
'''
#april 15 2021
from django.shortcuts import render, redirect

def Mainpage(request):
	if request.method == 'POST':
		Item.objects.create(text=request.post['personEntry'])
		return redirect ('/')

		items = Item.objects.all()

	
	return render(request, 'comment.html', {'newPerson':items})
	#return render(request, comment.html)


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
