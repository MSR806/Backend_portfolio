from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method =="POST":
        name= request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        query = request.POST['query']
        contact = Contact(name=name, email=email, phone=phone, query=query)
        contact.save()
        print('Data has been entered into the db')
    return render(request, 'contact.html')