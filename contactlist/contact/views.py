from django.shortcuts import render
from contact.models import contact,contactform

# Create your views here.
def homepage(request):
    return render(request,'home.html')
def contactpage(request):
   s=''
   if 'save' in request.POST:
       a_name=request.POST['name']
       a_email=request.POST['email']
       a_password=request.POST['password']
       a_contact=request.POST['contact']
       obj=contact(
           name=a_name,
           email=a_email,
           password=a_password,
           contact=a_contact
       )
       obj.save()
       s="Sucees"
   return render(request,'contact.html',{'sum':s})




