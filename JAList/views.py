from django.http import HttpResponse
from django.shortcuts import render, redirect
from JAList.models import Applicant, Studentinfo, School_Record, Scholarship, Status

def applicant(request):
	applicants=Applicant.objects.all()
	return render(request, 'applicant.html',{'applicants' : applicants})


def new_stuin(request): #1st
	newapplicant_=Applicant.objects.create(fname=request.POST['sname'],fschool=request.POST['school'])
	#return redirect(f'{newapplicant_.id}/')
	return redirect(f'{newapplicant_.id}/view_stuin')


def add_applicant(request, applicant_id): 
   applicant_ = Applicant.objects.get(id=applicant_id)    
   Studentinfo.objects.create(ggrade_year=request.POST['ysection'],gaddress=request.POST['address'],gcontactno=request.POST['cnumber'], applicant=applicant_)
   #return redirect(f'{applicant_.id}/') 
   return redirect(f'/{applicant_.id}/view_stuin') 


def view_stuin(request, applicant_id):  
	#studenti=Studentinfo.objects.all()
	applicant_ = Applicant.objects.get(id=applicant_id)
	return render(request, 'studentinfo.html', {'applicant': applicant_},)

#studentinfo 2nd


def student_info(request):
	applicants=Applicant.objects.all()
	return render(request, 'applicant.html',{'applicants' : applicants})


 

def edit(request, id):
	applicants=Applicant.objects.get(id=id)
	laman = {'applicants':applicants}
	return render(request, 'eapplicant.html', laman)

def update(request, id):
	applicant=Applicant.objects.get(id=id)
	applicant.fname=request.POST['sname']
	applicant.fschool=request.POST['school']
	applicant.save()
	return redirect('/')


def delete(request, id):
	applicant=Applicant.objects.get(id=id)
	applicant.delete()
	return redirect('/')


def sstudentinfo(request):
	return render (request, 'studentinfo.html')

def sschool_record(request):
	return render (request, 'schoolrecord.html')

def sscholarship(request):
	return render (request, 'scholarship.html')

def sstatus(request):
	return render (request, 'status.html')

'''

def add_item(request, applicant_id):
	applicant_=Applicant.objects.get(id=applicant_id)

	#Student_Information.objects.create(prComment=request.POST['private_comment'],mrate=request.POST['rate'], applicant=applicant_)
	return redirect(f'/JAList/{applicant_.id}')
'''


'''		
def view_list(request, list_id):
	applicant_= Applicant.objects.get(id=list_id)
	return render(request,'studentinfo.html',{ 'applicant' : applicant_ })
'''	
'''	

def new_list(request):
	applicant_ = Applicant.objects.create()
	
	#Student_Information.objects.create(cAuthor=request.POST['comment_author'], cEmail=request.POST['email'] , puComment=request.POST['public_comment'], list=list_ )	
	return redirect(f'/JAList/{applicant_.id}/')
'''



'''

def aapplicant(request):
	return render (request, 'applicant.html')

def sstudentinfo(request):
	return render (request, 'studentinfo.html')

def sschool_record(request):
	return render (request, 'schoolrecord.html')

def sscholarship(request):
	return render (request, 'scholarship.html')

def sstatus(request):
	return render (request, 'status.html')





def datamani(request):
	#creating
	applicant=Applicant(Name='Joice',School='TUPC')
	applicant.save()

	#read all entries
	objects=Applicant.all()
	result='Printing: <br>'
	for x in objects:
		res+= x.fname+ '<br>'

	#read specify
	sname=Applicant.objects.get(id='2')
	res += 'Printing <br>'
	res += Sname.Email

	#delete
	res += '<br> Delete <br>'
	sname.delete()

	#update
	applicant=Applicant(Name='Joice',School='TUPC')
	applicant.save()

	#filter
	qs = Student_Information.objects.get(Name='Joice')
	res += 'Found : %s results <br>'%len(de)

	#order
	qs = Applicant.order_by('Name')
	for x in de:
		res +=x.fname + x.fschool + '<br>'	

'''