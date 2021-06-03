from django.http import HttpResponse
from django.shortcuts import render, redirect
from JAList.models import Applicant, Student_Information


def home_page(request):
	student_informations=Student_Information.objects.all()
	return render(request, 'comment.html',{ 'student_informations' : student_informations })

def add_item(request, applicant_id):
	applicant_=Applicant.objects.get(id=applicant_id)

	#Student_Information.objects.create(prComment=request.POST['private_comment'],mrate=request.POST['rate'], applicant=applicant_)
	return redirect(f'/JAList/{applicant_.id}')
		
def view_list(request, list_id):
	applicant_= Applicant.objects.get(id=list_id)
	return render(request,'Rate.html',{ 'applicant' : applicant_ })
	
def new_list(request):
	applicant_ = Applicant.objects.create()
	
	#Student_Information.objects.create(cAuthor=request.POST['comment_author'], cEmail=request.POST['email'] , puComment=request.POST['public_comment'], list=list_ )	
	return redirect(f'/JAList/{applicant_.id}/')


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
