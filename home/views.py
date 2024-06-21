from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        DOB = request.POST['DOB']
        # print(name,phone,email,content)
        if len(name) < 3 or len(email) < 5 or len(phone) < 10 or len(content) < 3:
            messages.add_message(request, messages.WARNINGx, 'Fill the form Correctly')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content,DOB=DOB)
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'Thanks for filling the form')

    return render(request,'contact.html')
