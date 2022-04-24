from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
#from reportlab.lib.pagesizes import landscape
#from reportlab.platypus import Image
import os
from django.conf import settings
from django.http import HttpResponse
#from django.template.loader import get_template
#from xhtml2pdf import pisa
#from django.contrib.staticfiles import finders
import calendar
from calendar import HTMLCalendar
from DimosoApp.models import *
from DimosoApp.forms import *
#from hitcount.views import HitCountDetailView
from django.core.mail import send_mail
from django.conf import settings
from .send_sms import sendsms
from twilio.rest import Client
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def base(request):
	return render(request, "DimosoApp/base.html")
def home(request):
	return render(request, "DimosoApp/home.html")



def user_login(request):
    context={}
    if request.POST:
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user = authenticate(request, email=email,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            messages.success(request, "password or username is incorrect")
        else:
            context['login_form']=form
            
    else:
        #messages.success(request, "password or username is incorrect")
        form=UserLoginForm(request.POST)
        context['login_form']=form    
        
    return render(request,'DimosoApp/user_login.html', context)


def user_logout(request):
    logout(request)
    return redirect('user_login')
    return render(request,'DimosoApp/logout.html')

def registration(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"you are already authenticated as {user.email}")
    context = {}
    
    #form = MyUserForm()

    if request.POST:

        form=MyUserForm(request.POST)
        if form.is_valid():
            form.save()

            #HIZI NI KWA AJILI KUTUMA EMAIL ENDAPO MTU AKIJISAJILI
            username = request.POST['username']
            #last_name = request.POST['last_name']
            email = request.POST['email']
            subject = "Welcome to Dimoso El Blog"
            message = f"Thanks {username}  for registering in our system as {email} "
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            #ZINAISHIA HAPA ZA KUTUMA EMAIL



            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            myuser = authenticate(email=email,password=raw_password)
            if myuser is not None:
                         login(request,myuser)
                         #messages.success(request,"account created Successfully, now you can login.")
                         
                         return redirect('home')
            
            

        else:
            context['registration_form'] = form
        
            
        
           


    return render(request,'DimosoApp/registration.html', context)








def ReportIssues(request):
	form = ReportIssuesToParentForm()
	if request.method == 'POST':
		form = ReportIssuesToParentForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			send_through_email = request.POST['send_through_email']
			send_through_text = request.POST['send_through_text']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=send_through_text,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			#HIZI NIKWA AJILI YA KUTUMA EMAIL KWA MZAZI

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			
			send_through_email = request.POST['send_through_email']
			send_through_text = request.POST['send_through_text']
			
						
			html_content = render_to_string(
				"DimosoApp/issues_email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'send_through_email':send_through_email,
				"send_through_text":send_through_text
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'DimosoApp/ReportIssues.html', {"form":form})





























def all_form_one_reports(request):
	form = Form1ReportForm(request.POST or None)

	report = Form1Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'FormOne/all_form_one_reports.html', context)



    
def sending_email_to_form_one(request):
	form = Form1ReportForm()
	if request.method == 'POST':
		form = Form1ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'FormOne/sending_email_to_form_one.html', {"form":form})

def search_autoco_form_one_report(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = Form1Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_one_student(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = Form1Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_one_report(DetailView):
    model = Form1Report
    template_name = 'FormOne/view_form_one_report.html'
    
    

class update_form_one_report(SuccessMessageMixin, UpdateView):
    model = Form1Report
    template_name = 'FormOne/sending_email_to_form_one.html'
    form_class = Form1ReportForm
    success_url = reverse_lazy('all_form_one_reports')
    success_message = "Report Updated Successfully"  

def delete_form_one_report(request, pk):
    report = get_object_or_404(Form1Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_one_reports')

def all_form_one_students(request):
	form = Form1StudentsForm(request.POST or None)

	form1 = Form1Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form1":form1,
		"form":form

	}

	return render(request, 'FormOne/all_form_one_students.html', context)

def search_form1_student(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=Form1Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'FormOne/search_student.html',context)
	#hii ni kwa ajili ya kuserch form1 student then tunamdisplay kwenye page nyingine
def search_autoco_form_one_student2(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form1 = Form1Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form1]
    return JsonResponse(mylist, safe=False)  

class add_form1_students(SuccessMessageMixin, CreateView):
    model = Form1Students
    template_name = 'FormOne/add_form1_students.html'
    form_class = Form1StudentsForm
    success_url = reverse_lazy('all_form_one_students')
    success_message = "Form One Student  Added Successfully"

class update_form_one_student(SuccessMessageMixin, UpdateView):
    model = Form1Students
    template_name = 'FormOne/add_form1_students.html'
    form_class = Form1StudentsForm
    success_url = reverse_lazy('all_form_one_students')
    success_message = "Form One Student Updated Successfully"  

def delete_form_one_student(request, pk):
    student = get_object_or_404(Form1Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_one_students')


 #HIZI NIKWA AJILI YA CLASSES ZINAZOPATIKANA FORM ONE
def form1_A_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form1 = Form1Students.objects.filter(darasa__name__contains="A").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form1":form1,
		
		#"form":form

	}

	return render(request, 'FormOne/form1_A_students.html', context)

def form1_B_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form1 = Form1Students.objects.filter(darasa__name__contains="B").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form1":form1,
		
		#"form":form

	}

	return render(request, 'FormOne/form1_B_students.html', context)

def form1_C_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form1 = Form1Students.objects.filter(darasa__name__contains="C").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form1":form1,
		
		#"form":form

	}

	return render(request, 'FormOne/form1_C_students.html', context)
def form1_D_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form1 = Form1Students.objects.filter(darasa__name__contains="D").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form1":form1,
		
		#"form":form

	}

	return render(request, 'FormOne/form1_D_students.html', context)
def form1_E_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form1 = Form1Students.objects.filter(darasa__name__contains="E").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form1":form1,
		
		#"form":form

	}

	return render(request, 'FormOne/form1_E_students.html', context)





#FORM TWO VIEWS


def all_form_two_reports(request):
	form = Form2ReportForm(request.POST or None)

	report = Form2Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = Form2Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'FormTwo/all_form_two_reports.html', context)



    
def sending_email_to_form_two(request):
	form = Form2ReportForm()
	if request.method == 'POST':
		form = Form2ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'FormTwo/sending_email_to_form_two.html', {"form":form})

def search_autoco_form_two_report(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = Form2Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_two_student(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = Form2Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_two_report(DetailView):
    model = Form2Report
    template_name = 'FormTwo/view_form_two_report.html'
    
    

class update_form_two_report(SuccessMessageMixin, UpdateView):
    model = Form2Report
    template_name = 'FormTwo/sending_email_to_form_two.html'
    form_class = Form2ReportForm
    success_url = reverse_lazy('all_form_two_reports')
    success_message = "Report Updated Successfully"  

def delete_form_two_report(request, pk):
    report = get_object_or_404(Form2Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_two_reports')

def all_form_two_students(request):
	form = Form2StudentsForm(request.POST or None)

	form2 = Form2Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form2":form2,
		"form":form

	}

	return render(request, 'FormTwo/all_form_two_students.html', context)

def search_form2_student(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=Form2Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'FormTwo/search_student.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_two_student2(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form1 = Form2Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form1]
    return JsonResponse(mylist, safe=False)  

class add_form2_students(SuccessMessageMixin, CreateView):
    model = Form2Students
    template_name = 'FormTwo/add_form2_students.html'
    form_class = Form2StudentsForm
    success_url = reverse_lazy('all_form_two_students')
    success_message = "Form Two Student  Added Successfully"

class update_form_two_student(SuccessMessageMixin, UpdateView):
    model = Form2Students
    template_name = 'FormTwo/add_form2_students.html'
    form_class = Form2StudentsForm
    success_url = reverse_lazy('all_form_two_students')
    success_message = "Form Two Student Updated Successfully"  

def delete_form_two_student(request, pk):
    student = get_object_or_404(Form2Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_two_students')


 #HIZI NIKWA AJILI YA CLASSES ZINAZOPATIKANA FORM ONE
def form2_A_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form2 = Form2Students.objects.filter(darasa__name__contains="A").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form2":form2,
		
		#"form":form

	}

	return render(request, 'FormTwo/form2_A_students.html', context)

def form2_B_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form2 = Form2Students.objects.filter(darasa__name__contains="B").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form2":form2,
		
		#"form":form

	}

	return render(request, 'FormTwo/form2_B_students.html', context)

def form2_C_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form2 = Form2Students.objects.filter(darasa__name__contains="C").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form2":form2,
		
		#"form":form

	}

	return render(request, 'FormTwo/form2_C_students.html', context)
def form2_D_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form2 = Form2Students.objects.filter(darasa__name__contains="D").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form2":form2,
		
		#"form":form

	}

	return render(request, 'FormTwo/form2_D_students.html', context)
def form2_E_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form2 = Form2Students.objects.filter(darasa__name__contains="E").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form2":form2,
		
		#"form":form

	}

	return render(request, 'FormTwo/form2_E_students.html', context)





#FORM THREE VIEWS

def all_form_three_reports(request):
	form = Form3ReportForm(request.POST or None)

	report = Form3Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = Form3Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'FormThree/all_form_three_reports.html', context)



    
def sending_email_to_form_three(request):
	form = Form3ReportForm()
	if request.method == 'POST':
		form = Form3ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'FormThree/sending_email_to_form_three.html', {"form":form})

def search_autoco_form_three_report(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = Form3Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_three_student(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = Form3Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_three_report(DetailView):
    model = Form3Report
    template_name = 'FormThree/view_form_three_report.html'
    
    

class update_form_three_report(SuccessMessageMixin, UpdateView):
    model = Form3Report
    template_name = 'FormThree/sending_email_to_form_three.html'
    form_class = Form3ReportForm
    success_url = reverse_lazy('all_form_three_reports')
    success_message = "Report Updated Successfully"  

def delete_form_three_report(request, pk):
    report = get_object_or_404(Form3Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_three_reports')

def all_form_three_students(request):
	form = Form3StudentsForm(request.POST or None)

	form3 = Form3Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form3":form3,
		"form":form

	}

	return render(request, 'FormThree/all_form_three_students.html', context)

def search_form3_student(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=Form3Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'FormThree/search_student.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_three_student2(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form3 = Form3Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form3]
    return JsonResponse(mylist, safe=False)  

class add_form3_students(SuccessMessageMixin, CreateView):
    model = Form3Students
    template_name = 'FormThree/add_form3_students.html'
    form_class = Form3StudentsForm
    success_url = reverse_lazy('all_form_three_students')
    success_message = "Form Three Student  Added Successfully"

class update_form_three_student(SuccessMessageMixin, UpdateView):
    model = Form3Students
    template_name = 'FormThree/add_form3_students.html'
    form_class = Form3StudentsForm
    success_url = reverse_lazy('all_form_three_students')
    success_message = "Form Three Student Updated Successfully"  

def delete_form_three_student(request, pk):
    student = get_object_or_404(Form3Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_three_students')


 #HIZI NIKWA AJILI YA CLASSES ZINAZOPATIKANA FORM ONE
def form3_A_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form3 = Form3Students.objects.filter(darasa__name__contains="A").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form3":form3,
		
		#"form":form

	}

	return render(request, 'FormThree/form3_A_students.html', context)

def form3_B_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form3 = Form3Students.objects.filter(darasa__name__contains="B").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form3":form3,
		
		#"form":form

	}

	return render(request, 'FormThree/form3_B_students.html', context)

def form3_C_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form3 = Form3Students.objects.filter(darasa__name__contains="C").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form3":form3,
		
		#"form":form

	}

	return render(request, 'FormThree/form3_C_students.html', context)
def form3_D_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form3 = Form3Students.objects.filter(darasa__name__contains="D").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form3":form3,
		
		#"form":form

	}

	return render(request, 'FormThree/form3_D_students.html', context)
def form3_E_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form3 = Form3Students.objects.filter(darasa__name__contains="E").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form3":form3,
		
		#"form":form

	}

	return render(request, 'FormThree/form3_E_students.html', context)



#FORM FOUR VIEWS
def all_form_four_reports(request):
	form = Form4ReportForm(request.POST or None)

	report = Form4Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = Form4Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'FormFour/all_form_four_reports.html', context)



    
def sending_email_to_form_four(request):
	form = Form4ReportForm()
	if request.method == 'POST':
		form = Form4ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'FormFour/sending_email_to_form_four.html', {"form":form})

def search_autoco_form_four_report(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = Form4Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_four_student(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = Form4Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_four_report(DetailView):
    model = Form4Report
    template_name = 'FormFour/view_form_four_report.html'
    
    

class update_form_four_report(SuccessMessageMixin, UpdateView):
    model = Form4Report
    template_name = 'FormFour/sending_email_to_form_four.html'
    form_class = Form4ReportForm
    success_url = reverse_lazy('all_form_four_reports')
    success_message = "Report Updated Successfully"  

def delete_form_four_report(request, pk):
    report = get_object_or_404(Form4Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_four_reports')

def all_form_four_students(request):
	form = Form4StudentsForm(request.POST or None)

	form4 = Form4Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form4":form4,
		"form":form

	}

	return render(request, 'FormFour/all_form_four_students.html', context)

def search_form4_student(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=Form4Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'FormFour/search_student.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_four_student2(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form4 = Form4Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form4]
    return JsonResponse(mylist, safe=False)  

class add_form4_students(SuccessMessageMixin, CreateView):
    model = Form4Students
    template_name = 'FormFour/add_form4_students.html'
    form_class = Form4StudentsForm
    success_url = reverse_lazy('all_form_four_students')
    success_message = "Form Four Student  Added Successfully"

class update_form_four_student(SuccessMessageMixin, UpdateView):
    model = Form4Students
    template_name = 'FormFour/add_form4_students.html'
    form_class = Form4StudentsForm
    success_url = reverse_lazy('all_form_four_students')
    success_message = "Form Four Student Updated Successfully"  

def delete_form_four_student(request, pk):
    student = get_object_or_404(Form4Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_four_students')


 #HIZI NIKWA AJILI YA CLASSES ZINAZOPATIKANA FORM ONE
def form4_A_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form4 = Form4Students.objects.filter(darasa__name__contains="A").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form4":form4,
		
		#"form":form

	}

	return render(request, 'FormFour/form4_A_students.html', context)

def form4_B_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form4 = Form4Students.objects.filter(darasa__name__contains="B").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form4":form4,
		
		#"form":form

	}

	return render(request, 'FormFour/form4_B_students.html', context)

def form4_C_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form4 = Form4Students.objects.filter(darasa__name__contains="C").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form4":form4,
		
		#"form":form

	}

	return render(request, 'FormFour/form4_C_students.html', context)
def form4_D_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form4 = Form4Students.objects.filter(darasa__name__contains="D").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form4":form4,
		
		#"form":form

	}

	return render(request, 'FormFour/form4_D_students.html', context)
def form4_E_students(request):
	#form = Form1ReportForm(request.POST or None)
	

	form4 = Form4Students.objects.filter(darasa__name__contains="E").order_by('-id')
	#if request.method == 'POST':
	#report = Form1Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"form4":form4,
		
		#"form":form

	}

	return render(request, 'FormFour/form4_E_students.html', context)




#PCM FORM FIVE VIEWS

def all_form_five_reports_pcm(request):
	form = PcmForm5ReportForm(request.POST or None)

	report = PcmForm5Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = PcmForm5Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'PcmFormFive/all_form_five_reports_pcm.html', context)



    
def sending_email_to_form_five_pcm(request):
	form = PcmForm5ReportForm()
	if request.method == 'POST':
		form = PcmForm5ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'PcmFormFive/sending_email_to_form_five_pcm.html', {"form":form})

def search_autoco_form_five_report_pcm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PcmForm5Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_five_student_pcm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PcmForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_five_report_pcm(DetailView):
    model = PcmForm5Report
    template_name = 'PcmFormFive/view_form_five_report_pcm.html'
    
    

class update_form_five_report_pcm(SuccessMessageMixin, UpdateView):
    model = PcmForm5Report
    template_name = 'PcmFormFive/sending_email_to_form_five_pcm.html'
    form_class = PcmForm5ReportForm
    success_url = reverse_lazy('all_form_five_reports_pcm')
    success_message = "Report Updated Successfully"  

def delete_form_five_report_pcm(request, pk):
    report = get_object_or_404(PcmForm5Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_five_reports_pcm')

def all_form_five_students_pcm(request):
	form = PcmForm5StudentsForm(request.POST or None)

	form5 = PcmForm5Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'PcmFormFive/all_form_five_students_pcm.html', context)

def search_form5_student_pcm(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=PcmForm5Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'PcmFormFive/search_student_pcm.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_five_student2_pcm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = PcmForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form5_students_pcm(SuccessMessageMixin, CreateView):
    model = PcmForm5Students
    template_name = 'PcmFormFive/add_form5_students_pcm.html'
    form_class = PcmForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_pcm')
    success_message = "Form Five Pcm Student  Added Successfully"

class update_form_five_student_pcm(SuccessMessageMixin, UpdateView):
    model = PcmForm5Students
    template_name = 'PcmFormFive/add_form5_students_pcm.html'
    form_class = PcmForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_pcm')
    success_message = "Form Five Pcm Student Updated Successfully"  

def delete_form_five_student_pcm(request, pk):
    student = get_object_or_404(PcmForm5Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_five_students_pcm')


#PCB FORM 5 VIEWS
def all_form_five_reports_pcb(request):
	form = PcbForm5ReportForm(request.POST or None)

	report = PcbForm5Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = PcbForm5Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'PcbFormFive/all_form_five_reports_pcb.html', context)



    
def sending_email_to_form_five_pcb(request):
	form = PcbForm5ReportForm()
	if request.method == 'POST':
		form = PcbForm5ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'PcbFormFive/sending_email_to_form_five_pcb.html', {"form":form})

def search_autoco_form_five_report_pcb(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PcbForm5Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_five_student_pcb(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PcbForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_five_report_pcb(DetailView):
    model = PcbForm5Report
    template_name = 'PcbFormFive/view_form_five_report_pcb.html'
    
    

class update_form_five_report_pcb(SuccessMessageMixin, UpdateView):
    model = PcbForm5Report
    template_name = 'PcbFormFive/sending_email_to_form_five_pcb.html'
    form_class = PcbForm5ReportForm
    success_url = reverse_lazy('all_form_five_reports_pcb')
    success_message = "Report Updated Successfully"  

def delete_form_five_report_pcb(request, pk):
    report = get_object_or_404(PcbForm5Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_five_reports_pcb')

def all_form_five_students_pcb(request):
	form = PcbForm5StudentsForm(request.POST or None)

	form5 = PcbForm5Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'PcbFormFive/all_form_five_students_pcb.html', context)

def search_form5_student_pcb(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=PcbForm5Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'PcbFormFive/search_student_pcb.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_five_student2_pcb(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = PcbForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form5_students_pcb(SuccessMessageMixin, CreateView):
    model = PcbForm5Students
    template_name = 'PcbFormFive/add_form5_students_pcb.html'
    form_class = PcbForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_pcb')
    success_message = "Form Five Pcb Student  Added Successfully"

class update_form_five_student_pcb(SuccessMessageMixin, UpdateView):
    model = PcbForm5Students
    template_name = 'PcbFormFive/add_form5_students_pcb.html'
    form_class = PcbForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_pcb')
    success_message = "Form Five Pcb Student Updated Successfully"  

def delete_form_five_student_pcb(request, pk):
    student = get_object_or_404(PcbForm5Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_five_students_pcb')



#PGM FORM 5 VIEWS
def all_form_five_reports_pgm(request):
	form = PgmForm5ReportForm(request.POST or None)

	report = PgmForm5Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = PgmForm5Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'PgmFormFive/all_form_five_reports_pgm.html', context)



    
def sending_email_to_form_five_pgm(request):
	form = PgmForm5ReportForm()
	if request.method == 'POST':
		form = PgmForm5ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'PgmFormFive/sending_email_to_form_five_pgm.html', {"form":form})

def search_autoco_form_five_report_pgm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PgmForm5Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_five_student_pgm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PgmForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_five_report_pgm(DetailView):
    model = PgmForm5Report
    template_name = 'PgmFormFive/view_form_five_report_pgm.html'
    
    

class update_form_five_report_pgm(SuccessMessageMixin, UpdateView):
    model = PgmForm5Report
    template_name = 'PgmFormFive/sending_email_to_form_five_pgm.html'
    form_class = PgmForm5ReportForm
    success_url = reverse_lazy('all_form_five_reports_pgm')
    success_message = "Report Updated Successfully"  

def delete_form_five_report_pgm(request, pk):
    report = get_object_or_404(PgmForm5Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_five_reports_pgm')

def all_form_five_students_pgm(request):
	form = PgmForm5StudentsForm(request.POST or None)

	form5 = PgmForm5Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'PgmFormFive/all_form_five_students_pgm.html', context)

def search_form5_student_pgm(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=PgmForm5Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'PgmFormFive/search_student_pgm.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_five_student2_pgm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = PgmForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form5_students_pgm(SuccessMessageMixin, CreateView):
    model = PgmForm5Students
    template_name = 'PgmFormFive/add_form5_students_pgm.html'
    form_class = PgmForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_pgm')
    success_message = "Form Five Pgm Student  Added Successfully"

class update_form_five_student_pgm(SuccessMessageMixin, UpdateView):
    model = PgmForm5Students
    template_name = 'PgmFormFive/add_form5_students_pgm.html'
    form_class = PgmForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_pgm')
    success_message = "Form Five Pgm Student Updated Successfully"  

def delete_form_five_student_pgm(request, pk):
    student = get_object_or_404(PgmForm5Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_five_students_pgm')







#HGL FORM 5 VIEWS
def all_form_five_reports_hgl(request):
	form = HglForm5ReportForm(request.POST or None)

	report = HglForm5Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = HglForm5Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'HglFormFive/all_form_five_reports_hgl.html', context)



    
def sending_email_to_form_five_hgl(request):
	form = HglForm5ReportForm()
	if request.method == 'POST':
		form = HglForm5ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'HglFormFive/sending_email_to_form_five_hgl.html', {"form":form})

def search_autoco_form_five_report_hgl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HglForm5Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_five_student_hgl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HglForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_five_report_hgl(DetailView):
    model = HglForm5Report
    template_name = 'HglFormFive/view_form_five_report_hgl.html'
    
    

class update_form_five_report_hgl(SuccessMessageMixin, UpdateView):
    model = HglForm5Report
    template_name = 'HglFormFive/sending_email_to_form_five_hgl.html'
    form_class = HglForm5ReportForm
    success_url = reverse_lazy('all_form_five_reports_hgl')
    success_message = "Report Updated Successfully"  

def delete_form_five_report_hgl(request, pk):
    report = get_object_or_404(HglForm5Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_five_reports_hgl')

def all_form_five_students_hgl(request):
	form = HglForm5StudentsForm(request.POST or None)

	form5 = HglForm5Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'HglFormFive/all_form_five_students_hgl.html', context)

def search_form5_student_hgl(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=HglForm5Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'HglFormFive/search_student_hgl.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_five_student2_hgl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = HglForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form5_students_hgl(SuccessMessageMixin, CreateView):
    model = HglForm5Students
    template_name = 'HglFormFive/add_form5_students_hgl.html'
    form_class = HglForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_hgl')
    success_message = "Form Five Hgl Student  Added Successfully"

class update_form_five_student_hgl(SuccessMessageMixin, UpdateView):
    model = HglForm5Students
    template_name = 'HglFormFive/add_form5_students_hgl.html'
    form_class = HglForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_hgl')
    success_message = "Form Five Hgl Student Updated Successfully"  

def delete_form_five_student_hgl(request, pk):
    student = get_object_or_404(HglForm5Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_five_students_hgl')


  #HGK FORM 5 VIEWS

def all_form_five_reports_hgk(request):
	form = HgkForm5ReportForm(request.POST or None)

	report = HgkForm5Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = HgkForm5Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'HgkFormFive/all_form_five_reports_hgk.html', context)



    
def sending_email_to_form_five_hgk(request):
	form = HgkForm5ReportForm()
	if request.method == 'POST':
		form = HgkForm5ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'HgkFormFive/sending_email_to_form_five_hgk.html', {"form":form})

def search_autoco_form_five_report_hgk(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HgkForm5Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_five_student_hgk(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HgkForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_five_report_hgk(DetailView):
    model = HgkForm5Report
    template_name = 'HgkFormFive/view_form_five_report_hgk.html'
    
    

class update_form_five_report_hgk(SuccessMessageMixin, UpdateView):
    model = HgkForm5Report
    template_name = 'HgkFormFive/sending_email_to_form_five_hgk.html'
    form_class = HgkForm5ReportForm
    success_url = reverse_lazy('all_form_five_reports_hgk')
    success_message = "Report Updated Successfully"  

def delete_form_five_report_hgk(request, pk):
    report = get_object_or_404(HgkForm5Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_five_reports_hgk')

def all_form_five_students_hgk(request):
	form = HgkForm5StudentsForm(request.POST or None)

	form5 = HgkForm5Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'HgkFormFive/all_form_five_students_hgk.html', context)

def search_form5_student_hgk(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=HgkForm5Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'HgkFormFive/search_student_hgk.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_five_student2_hgk(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = HgkForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form5_students_hgk(SuccessMessageMixin, CreateView):
    model = HgkForm5Students
    template_name = 'HgkFormFive/add_form5_students_hgk.html'
    form_class = HgkForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_hgk')
    success_message = "Form Five Hgk Student  Added Successfully"

class update_form_five_student_hgk(SuccessMessageMixin, UpdateView):
    model = HgkForm5Students
    template_name = 'HgkFormFive/add_form5_students_hgk.html'
    form_class = HgkForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_hgk')
    success_message = "Form Five Hgk Student Updated Successfully"  

def delete_form_five_student_hgk(request, pk):
    student = get_object_or_404(HgkForm5Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_five_students_hgk')


#CBG FORM 5 VIEWS

def all_form_five_reports_cbg(request):
	form = CbgForm5ReportForm(request.POST or None)

	report = CbgForm5Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = CbgForm5Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'CbgFormFive/all_form_five_reports_cbg.html', context)



    
def sending_email_to_form_five_cbg(request):
	form = CbgForm5ReportForm()
	if request.method == 'POST':
		form = CbgForm5ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'CbgFormFive/sending_email_to_form_five_cbg.html', {"form":form})

def search_autoco_form_five_report_cbg(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = CbgForm5Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_five_student_cbg(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = CbgForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_five_report_cbg(DetailView):
    model = CbgForm5Report
    template_name = 'CbgFormFive/view_form_five_report_cbg.html'
    
    

class update_form_five_report_cbg(SuccessMessageMixin, UpdateView):
    model = CbgForm5Report
    template_name = 'CbgFormFive/sending_email_to_form_five_cbg.html'
    form_class = CbgForm5ReportForm
    success_url = reverse_lazy('all_form_five_reports_cbg')
    success_message = "Report Updated Successfully"  

def delete_form_five_report_cbg(request, pk):
    report = get_object_or_404(CbgForm5Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_five_reports_cbg')

def all_form_five_students_cbg(request):
	form = CbgForm5StudentsForm(request.POST or None)

	form5 = CbgForm5Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'CbgFormFive/all_form_five_students_cbg.html', context)

def search_form5_student_cbg(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=CbgForm5Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'CbgFormFive/search_student_cbg.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_five_student2_cbg(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = CbgForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form5_students_cbg(SuccessMessageMixin, CreateView):
    model = CbgForm5Students
    template_name = 'CbgFormFive/add_form5_students_cbg.html'
    form_class = CbgForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_cbg')
    success_message = "Form Five Cbg Student  Added Successfully"

class update_form_five_student_cbg(SuccessMessageMixin, UpdateView):
    model = CbgForm5Students
    template_name = 'CbgFormFive/add_form5_students_cbg.html'
    form_class = CbgForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_cbg')
    success_message = "Form Five Cbg Student Updated Successfully"  

def delete_form_five_student_cbg(request, pk):
    student = get_object_or_404(CbgForm5Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_five_students_cbg')


  #HKL FORM 5 VIEWS

def all_form_five_reports_hkl(request):
	form = HklForm5ReportForm(request.POST or None)

	report = HklForm5Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = HklForm5Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'HklFormFive/all_form_five_reports_hkl.html', context)



    
def sending_email_to_form_five_hkl(request):
	form = HklForm5ReportForm()
	if request.method == 'POST':
		form = HklForm5ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'HklFormFive/sending_email_to_form_five_hkl.html', {"form":form})

def search_autoco_form_five_report_hkl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HklForm5Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_five_student_hkl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HklForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_five_report_hkl(DetailView):
    model = HklForm5Report
    template_name = 'HklFormFive/view_form_five_report_hkl.html'
    
    

class update_form_five_report_hkl(SuccessMessageMixin, UpdateView):
    model = HklForm5Report
    template_name = 'HklFormFive/sending_email_to_form_five_hkl.html'
    form_class = HklForm5ReportForm
    success_url = reverse_lazy('all_form_five_reports_hkl')
    success_message = "Report Updated Successfully"  

def delete_form_five_report_hkl(request, pk):
    report = get_object_or_404(HklForm5Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_five_reports_hkl')

def all_form_five_students_hkl(request):
	form = HklForm5StudentsForm(request.POST or None)

	form5 = HklForm5Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'HklFormFive/all_form_five_students_hkl.html', context)

def search_form5_student_hkl(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=HklForm5Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'HklFormFive/search_student_hkl.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_five_student2_hkl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = HklForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form5_students_hkl(SuccessMessageMixin, CreateView):
    model = HklForm5Students
    template_name = 'HklFormFive/add_form5_students_hkl.html'
    form_class = HklForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_hkl')
    success_message = "Form Five Hkl Student  Added Successfully"

class update_form_five_student_hkl(SuccessMessageMixin, UpdateView):
    model = HklForm5Students
    template_name = 'HklFormFive/add_form5_students_hkl.html'
    form_class = HklForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_hkl')
    success_message = "Form Five Hkl Student Updated Successfully"  

def delete_form_five_student_hkl(request, pk):
    student = get_object_or_404(HklForm5Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_five_students_hkl')


  # ECA FORM 5 VIEWS
def all_form_five_reports_eca(request):
	form = EcaForm5ReportForm(request.POST or None)

	report = EcaForm5Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = EcaForm5Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'EcaFormFive/all_form_five_reports_eca.html', context)



    
def sending_email_to_form_five_eca(request):
	form = EcaForm5ReportForm()
	if request.method == 'POST':
		form = EcaForm5ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'EcaFormFive/sending_email_to_form_five_eca.html', {"form":form})

def search_autoco_form_five_report_eca(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = EcaForm5Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_five_student_eca(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = EcaForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_five_report_eca(DetailView):
    model = EcaForm5Report
    template_name = 'EcaFormFive/view_form_five_report_eca.html'
    
    

class update_form_five_report_eca(SuccessMessageMixin, UpdateView):
    model = EcaForm5Report
    template_name = 'EcaFormFive/sending_email_to_form_five_eca.html'
    form_class = EcaForm5ReportForm
    success_url = reverse_lazy('all_form_five_reports_eca')
    success_message = "Report Updated Successfully"  

def delete_form_five_report_eca(request, pk):
    report = get_object_or_404(EcaForm5Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_five_reports_eca')

def all_form_five_students_eca(request):
	form = EcaForm5StudentsForm(request.POST or None)

	form5 = EcaForm5Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'EcaFormFive/all_form_five_students_eca.html', context)

def search_form5_student_eca(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=EcaForm5Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'EcaFormFive/search_student_eca.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_five_student2_eca(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = EcaForm5Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form5_students_eca(SuccessMessageMixin, CreateView):
    model = EcaForm5Students
    template_name = 'EcaFormFive/add_form5_students_eca.html'
    form_class = EcaForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_eca')
    success_message = "Form Five Eca Student  Added Successfully"

class update_form_five_student_eca(SuccessMessageMixin, UpdateView):
    model = EcaForm5Students
    template_name = 'EcaFormFive/add_form5_students_eca.html'
    form_class = EcaForm5StudentsForm
    success_url = reverse_lazy('all_form_five_students_eca')
    success_message = "Form Five Eca Student Updated Successfully"  

def delete_form_five_student_eca(request, pk):
    student = get_object_or_404(EcaForm5Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_five_students_eca')






















#FORM SIX VIEWS form 6 FORM 6 FORM 6 FORM 6 FORM 6 FORM 6

def all_form_six_reports_pcm(request):
	form = PcmForm6ReportForm(request.POST or None)

	report = PcmForm6Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = PcmForm6Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'PcmFormSix/all_form_six_reports_pcm.html', context)



    
def sending_email_to_form_six_pcm(request):
	form = PcmForm6ReportForm()
	if request.method == 'POST':
		form = PcmForm6ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'PcmFormSix/sending_email_to_form_six_pcm.html', {"form":form})

def search_autoco_form_six_report_pcm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PcmForm6Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_six_student_pcm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PcmForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_six_report_pcm(DetailView):
    model = PcmForm6Report
    template_name = 'PcmFormSix/view_form_six_report_pcm.html'
    
    

class update_form_six_report_pcm(SuccessMessageMixin, UpdateView):
    model = PcmForm6Report
    template_name = 'PcmFormSix/sending_email_to_form_six_pcm.html'
    form_class = PcmForm6ReportForm
    success_url = reverse_lazy('all_form_six_reports_pcm')
    success_message = "Report Updated Successfully"  

def delete_form_six_report_pcm(request, pk):
    report = get_object_or_404(PcmForm6Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_six_reports_pcm')

def all_form_six_students_pcm(request):
	form = PcmForm6StudentsForm(request.POST or None)

	form5 = PcmForm6Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'PcmFormSix/all_form_six_students_pcm.html', context)

def search_form6_student_pcm(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=PcmForm6Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'PcmFormSix/search_student_pcm.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_six_student2_pcm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = PcmForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form6_students_pcm(SuccessMessageMixin, CreateView):
    model = PcmForm6Students
    template_name = 'PcmFormSix/add_form6_students_pcm.html'
    form_class = PcmForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_pcm')
    success_message = "Form Six Pcm Student  Added Successfully"

class update_form_six_student_pcm(SuccessMessageMixin, UpdateView):
    model = PcmForm6Students
    template_name = 'PcmFormSix/add_form6_students_pcm.html'
    form_class = PcmForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_pcm')
    success_message = "Form Six Pcm Student Updated Successfully"  

def delete_form_six_student_pcm(request, pk):
    student = get_object_or_404(PcmForm6Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_six_students_pcm')


#PCB FORM 5 VIEWS
def all_form_six_reports_pcb(request):
	form = PcbForm6ReportForm(request.POST or None)

	report = PcbForm6Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = PcbForm6Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'PcbFormSix/all_form_six_reports_pcb.html', context)



    
def sending_email_to_form_six_pcb(request):
	form = PcbForm6ReportForm()
	if request.method == 'POST':
		form = PcbForm6ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'PcbFormSix/sending_email_to_form_six_pcb.html', {"form":form})

def search_autoco_form_six_report_pcb(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PcbForm6Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_six_student_pcb(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PcbForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_six_report_pcb(DetailView):
    model = PcbForm6Report
    template_name = 'PcbFormSix/view_form_six_report_pcb.html'
    
    

class update_form_six_report_pcb(SuccessMessageMixin, UpdateView):
    model = PcbForm6Report
    template_name = 'PcbFormSix/sending_email_to_form_six_pcb.html'
    form_class = PcbForm6ReportForm
    success_url = reverse_lazy('all_form_six_reports_pcb')
    success_message = "Report Updated Successfully"  

def delete_form_six_report_pcb(request, pk):
    report = get_object_or_404(PcbForm6Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_six_reports_pcb')

def all_form_six_students_pcb(request):
	form = PcbForm6StudentsForm(request.POST or None)

	form5 = PcbForm6Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'PcbFormSix/all_form_six_students_pcb.html', context)

def search_form6_student_pcb(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=PcbForm6Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'PcbFormSix/search_student_pcb.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_six_student2_pcb(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = PcbForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form6_students_pcb(SuccessMessageMixin, CreateView):
    model = PcbForm6Students
    template_name = 'PcbFormSix/add_form6_students_pcb.html'
    form_class = PcbForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_pcb')
    success_message = "Form Six Pcb Student  Added Successfully"

class update_form_six_student_pcb(SuccessMessageMixin, UpdateView):
    model = PcbForm6Students
    template_name = 'PcbFormSix/add_form6_students_pcb.html'
    form_class = PcbForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_pcb')
    success_message = "Form Six Pcb Student Updated Successfully"  

def delete_form_six_student_pcb(request, pk):
    student = get_object_or_404(PcbForm6Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_six_students_pcb')



#PGM FORM 5 VIEWS
def all_form_six_reports_pgm(request):
	form = PgmForm6ReportForm(request.POST or None)

	report = PgmForm6Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = PgmForm6Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'PgmFormSix/all_form_six_reports_pgm.html', context)



    
def sending_email_to_form_six_pgm(request):
	form = PgmForm6ReportForm()
	if request.method == 'POST':
		form = PgmForm6ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'PgmFormSix/sending_email_to_form_six_pgm.html', {"form":form})

def search_autoco_form_six_report_pgm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PgmForm6Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_six_student_pgm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = PgmForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_six_report_pgm(DetailView):
    model = PgmForm6Report
    template_name = 'PgmFormSix/view_form_six_report_pgm.html'
    
    

class update_form_six_report_pgm(SuccessMessageMixin, UpdateView):
    model = PgmForm6Report
    template_name = 'PgmFormSix/sending_email_to_form_six_pgm.html'
    form_class = PgmForm6ReportForm
    success_url = reverse_lazy('all_form_six_reports_pgm')
    success_message = "Report Updated Successfully"  

def delete_form_six_report_pgm(request, pk):
    report = get_object_or_404(PgmForm6Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_six_reports_pgm')

def all_form_six_students_pgm(request):
	form = PgmForm6StudentsForm(request.POST or None)

	form5 = PgmForm6Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'PgmFormSix/all_form_six_students_pgm.html', context)

def search_form6_student_pgm(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=PgmForm6Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'PgmFormSix/search_student_pgm.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_six_student2_pgm(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = PgmForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form6_students_pgm(SuccessMessageMixin, CreateView):
    model = PgmForm6Students
    template_name = 'PgmFormSix/add_form6_students_pgm.html'
    form_class = PgmForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_pgm')
    success_message = "Form Six Pgm Student  Added Successfully"

class update_form_six_student_pgm(SuccessMessageMixin, UpdateView):
    model = PgmForm6Students
    template_name = 'PgmFormSix/add_form6_students_pgm.html'
    form_class = PgmForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_pgm')
    success_message = "Form Six Pgm Student Updated Successfully"  

def delete_form_six_student_pgm(request, pk):
    student = get_object_or_404(PgmForm6Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_six_students_pgm')







#HGL FORM 5 VIEWS
def all_form_six_reports_hgl(request):
	form = HglForm6ReportForm(request.POST or None)

	report = HglForm6Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = HglForm6Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'HglFormSix/all_form_six_reports_hgl.html', context)



    
def sending_email_to_form_six_hgl(request):
	form = HglForm6ReportForm()
	if request.method == 'POST':
		form = HglForm6ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'HglFormSix/sending_email_to_form_six_hgl.html', {"form":form})

def search_autoco_form_six_report_hgl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HglForm6Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_six_student_hgl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HglForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_six_report_hgl(DetailView):
    model = HglForm6Report
    template_name = 'HglFormSix/view_form_six_report_hgl.html'
    
    

class update_form_six_report_hgl(SuccessMessageMixin, UpdateView):
    model = HglForm6Report
    template_name = 'HglFormSix/sending_email_to_form_six_hgl.html'
    form_class = HglForm6ReportForm
    success_url = reverse_lazy('all_form_six_reports_hgl')
    success_message = "Report Updated Successfully"  

def delete_form_six_report_hgl(request, pk):
    report = get_object_or_404(HglForm6Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_six_reports_hgl')

def all_form_six_students_hgl(request):
	form = HglForm6StudentsForm(request.POST or None)

	form5 = HglForm6Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'HglFormSix/all_form_six_students_hgl.html', context)

def search_form6_student_hgl(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=HglForm6Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'HglFormSix/search_student_hgl.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_six_student2_hgl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = HglForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form6_students_hgl(SuccessMessageMixin, CreateView):
    model = HglForm6Students
    template_name = 'HglFormSix/add_form6_students_hgl.html'
    form_class = HglForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_hgl')
    success_message = "Form Six Hgl Student  Added Successfully"

class update_form_six_student_hgl(SuccessMessageMixin, UpdateView):
    model = HglForm6Students
    template_name = 'HglFormSix/add_form6_students_hgl.html'
    form_class = HglForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_hgl')
    success_message = "Form Six Hgl Student Updated Successfully"  

def delete_form_six_student_hgl(request, pk):
    student = get_object_or_404(HglForm6Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_six_students_hgl')


  #HGK FORM 5 VIEWS

def all_form_six_reports_hgk(request):
	form = HgkForm6ReportForm(request.POST or None)

	report = HgkForm6Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = HgkForm6Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'HgkFormSix/all_form_six_reports_hgk.html', context)



    
def sending_email_to_form_six_hgk(request):
	form = HgkForm6ReportForm()
	if request.method == 'POST':
		form = HgkForm6ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'HgkFormSix/sending_email_to_form_six_hgk.html', {"form":form})

def search_autoco_form_six_report_hgk(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HgkForm6Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_six_student_hgk(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HgkForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_six_report_hgk(DetailView):
    model = HgkForm6Report
    template_name = 'HgkFormSix/view_form_six_report_hgk.html'
    
    

class update_form_six_report_hgk(SuccessMessageMixin, UpdateView):
    model = HgkForm6Report
    template_name = 'HgkFormSix/sending_email_to_form_six_hgk.html'
    form_class = HgkForm6ReportForm
    success_url = reverse_lazy('all_form_six_reports_hgk')
    success_message = "Report Updated Successfully"  

def delete_form_six_report_hgk(request, pk):
    report = get_object_or_404(HgkForm6Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_six_reports_hgk')

def all_form_six_students_hgk(request):
	form = HgkForm6StudentsForm(request.POST or None)

	form5 = HgkForm6Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'HgkFormSix/all_form_six_students_hgk.html', context)

def search_form6_student_hgk(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=HgkForm6Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'HgkFormSix/search_student_hgk.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_six_student2_hgk(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = HgkForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form6_students_hgk(SuccessMessageMixin, CreateView):
    model = HgkForm6Students
    template_name = 'HgkFormSix/add_form6_students_hgk.html'
    form_class = HgkForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_hgk')
    success_message = "Form Six Hgk Student  Added Successfully"

class update_form_six_student_hgk(SuccessMessageMixin, UpdateView):
    model = HgkForm6Students
    template_name = 'HgkFormSix/add_form6_students_hgk.html'
    form_class = HgkForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_hgk')
    success_message = "Form Six Hgk Student Updated Successfully"  

def delete_form_six_student_hgk(request, pk):
    student = get_object_or_404(HgkForm6Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_six_students_hgk')


#CBG FORM 5 VIEWS

def all_form_six_reports_cbg(request):
	form = CbgForm6ReportForm(request.POST or None)

	report = CbgForm6Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = CbgForm6Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'CbgFormSix/all_form_six_reports_cbg.html', context)



    
def sending_email_to_form_six_cbg(request):
	form = CbgForm6ReportForm()
	if request.method == 'POST':
		form = CbgForm6ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'CbgFormSix/sending_email_to_form_six_cbg.html', {"form":form})

def search_autoco_form_six_report_cbg(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = CbgForm6Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_six_student_cbg(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = CbgForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_six_report_cbg(DetailView):
    model = CbgForm6Report
    template_name = 'CbgFormSix/view_form_six_report_cbg.html'
    
    

class update_form_six_report_cbg(SuccessMessageMixin, UpdateView):
    model = CbgForm6Report
    template_name = 'CbgFormSix/sending_email_to_form_six_cbg.html'
    form_class = CbgForm6ReportForm
    success_url = reverse_lazy('all_form_six_reports_cbg')
    success_message = "Report Updated Successfully"  

def delete_form_six_report_cbg(request, pk):
    report = get_object_or_404(CbgForm6Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_six_reports_cbg')

def all_form_six_students_cbg(request):
	form = CbgForm6StudentsForm(request.POST or None)

	form5 = CbgForm6Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'CbgFormSix/all_form_six_students_cbg.html', context)

def search_form6_student_cbg(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=CbgForm6Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'CbgFormSix/search_student_cbg.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_six_student2_cbg(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = CbgForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form6_students_cbg(SuccessMessageMixin, CreateView):
    model = CbgForm6Students
    template_name = 'CbgFormSix/add_form6_students_cbg.html'
    form_class = CbgForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_cbg')
    success_message = "Form Six Cbg Student  Added Successfully"

class update_form_six_student_cbg(SuccessMessageMixin, UpdateView):
    model = CbgForm6Students
    template_name = 'CbgFormSix/add_form6_students_cbg.html'
    form_class = CbgForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_cbg')
    success_message = "Form Six Cbg Student Updated Successfully"  

def delete_form_six_student_cbg(request, pk):
    student = get_object_or_404(CbgForm6Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_six_students_cbg')


  #HKL FORM 5 VIEWS

def all_form_six_reports_hkl(request):
	form = HklForm6ReportForm(request.POST or None)

	report = HklForm6Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = HklForm6Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'HklFormSix/all_form_six_reports_hkl.html', context)



    
def sending_email_to_form_six_hkl(request):
	form = HklForm6ReportForm()
	if request.method == 'POST':
		form = HklForm6ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'HklFormSix/sending_email_to_form_six_hkl.html', {"form":form})

def search_autoco_form_six_report_hkl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HklForm6Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_six_student_hkl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = HklForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_six_report_hkl(DetailView):
    model = HklForm6Report
    template_name = 'HklFormSix/view_form_six_report_hkl.html'
    
    

class update_form_six_report_hkl(SuccessMessageMixin, UpdateView):
    model = HklForm6Report
    template_name = 'HklFormSix/sending_email_to_form_six_hkl.html'
    form_class = HklForm6ReportForm
    success_url = reverse_lazy('all_form_six_reports_hkl')
    success_message = "Report Updated Successfully"  

def delete_form_six_report_hkl(request, pk):
    report = get_object_or_404(HklForm6Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_six_reports_hkl')

def all_form_six_students_hkl(request):
	form = HklForm6StudentsForm(request.POST or None)

	form5 = HklForm6Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'HklFormSix/all_form_six_students_hkl.html', context)

def search_form6_student_hkl(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=HklForm6Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'HklFormSix/search_student_hkl.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_six_student2_hkl(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = HklForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form6_students_hkl(SuccessMessageMixin, CreateView):
    model = HklForm6Students
    template_name = 'HklFormSix/add_form6_students_hkl.html'
    form_class = HklForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_hkl')
    success_message = "Form Six Hkl Student  Added Successfully"

class update_form_six_student_hkl(SuccessMessageMixin, UpdateView):
    model = HklForm6Students
    template_name = 'HklFormSix/add_form6_students_hkl.html'
    form_class = HklForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_hkl')
    success_message = "Form Six Hkl Student Updated Successfully"  

def delete_form_six_student_hkl(request, pk):
    student = get_object_or_404(HklForm6Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_six_students_hkl')


  # ECA FORM 5 VIEWS
def all_form_six_reports_eca(request):
	form = EcaForm6ReportForm(request.POST or None)

	report = EcaForm6Report.objects.all().order_by('-id')
	if request.method == 'POST':
		report = EcaForm6Report.objects.filter( name__icontains=form['name'].value())

	context = {
		"report":report,
		"form":form

	}

	return render(request, 'EcaFormSix/all_form_six_reports_eca.html', context)



    
def sending_email_to_form_six_eca(request):
	form = EcaForm6ReportForm()
	if request.method == 'POST':
		form = EcaForm6ReportForm(request.POST)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST['name']
			phone = request.POST['phone']
			bodyy = request.POST['body']
			description = request.POST['description']

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "b6c2b89770b828083644d3ad215a1d7c"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=description,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			to = request.POST['email']
			name = request.POST['name']
			phone = request.POST['phone']
			body = request.POST['body']
			description = request.POST['description']
			
						
			html_content = render_to_string(
				"DimosoApp/email_template.html",
				{
				'title':'Student Report System ', 
				'name':name,
				'phone':phone,
				'body':body,
				"description":description
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)
			return redirect('home')
		#context={
			#"title":'send email'
		#}
	return render(request, 'EcaFormSix/sending_email_to_form_six_eca.html', {"form":form})

def search_autoco_form_six_report_eca(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = EcaForm6Report.objects.filter(search)
    mylist= []
    mylist += [x.name for x in report]
    return JsonResponse(mylist, safe=False)  
def search_autoco_form_six_student_eca(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    report = EcaForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.fname+ " " + " " + x.sname+ " " + x.lname for x in report]
    return JsonResponse(mylist, safe=False)  

class view_form_six_report_eca(DetailView):
    model = EcaForm6Report
    template_name = 'EcaFormSix/view_form_six_report_eca.html'
    
    

class update_form_six_report_eca(SuccessMessageMixin, UpdateView):
    model = EcaForm6Report
    template_name = 'EcaFormSix/sending_email_to_form_six_eca.html'
    form_class = EcaForm6ReportForm
    success_url = reverse_lazy('all_form_six_reports_eca')
    success_message = "Report Updated Successfully"  

def delete_form_six_report_eca(request, pk):
    report = get_object_or_404(EcaForm6Report, id=pk)
    report.delete()
    messages.success(request, "Report Deleted Successfully")
    return redirect('all_form_six_reports_eca')

def all_form_six_students_eca(request):
	form = EcaForm6StudentsForm(request.POST or None)

	form5 = EcaForm6Students.objects.all().order_by('-id')
	#if request.method == 'POST':
		#form1 = Form1Students.objects.filter( lname__icontains=form['lname'].value())

	context = {
		"form5":form5,
		"form":form

	}

	return render(request, 'EcaFormSix/all_form_six_students_eca.html', context)

def search_form6_student_eca(request):
	query=None
	results=[]
	if request.method == "GET":
		query=request.GET.get("search")
		results=EcaForm6Students.objects.filter(Q(fname__icontains=query)|Q(sname__icontains=query)|Q(lname__icontains=query))
	context={
		"query":query,
		"results":results
	}
	return render(request, 'EcaFormSix/search_student_eca.html',context)
	#hii ni kwa ajili ya kuserch form2 student then tunamdisplay kwenye page nyingine
def search_autoco_form_six_student2_eca(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(fname__icontains=query_original) | Q(sname__icontains=query_original) | Q(lname__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    form5 = EcaForm6Students.objects.filter(search)
    mylist= []
    mylist += [x.lname for x in form5]
    return JsonResponse(mylist, safe=False)  

class add_form6_students_eca(SuccessMessageMixin, CreateView):
    model = EcaForm6Students
    template_name = 'EcaFormSix/add_form6_students_eca.html'
    form_class = EcaForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_eca')
    success_message = "Form Six Eca Student  Added Successfully"

class update_form_six_student_eca(SuccessMessageMixin, UpdateView):
    model = EcaForm6Students
    template_name = 'EcaFormSix/add_form6_students_eca.html'
    form_class = EcaForm6StudentsForm
    success_url = reverse_lazy('all_form_six_students_eca')
    success_message = "Form Six Eca Student Updated Successfully"  

def delete_form_six_student_eca(request, pk):
    student = get_object_or_404(EcaForm6Students, id=pk)
    student.delete()
    messages.success(request, "Student Deleted Successfully")
    return redirect('all_form_six_students_eca')


