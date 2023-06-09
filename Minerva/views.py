from django.shortcuts import render
from Minerva.models import Submit_Data
from django.contrib import messages


# Create your views here.


def about(request):
    Content = {
        "home": "",
        "about": "active",
        "contact": ""
    }

    return render(request, 'About.html', Content)


def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        message = request.POST.get('message')
        save_Data = Submit_Data(Email=email, Message=message)
        save_Data.save()
        messages.success(request, "You message has been sent !")

    Content = {
        "home": "",
        "about": "",
        "contact": "active"
    }

    return render(request, 'Contact.html', Content)


def home(request):
    Content = {
        "home": "active",
        "about": "",
        "contact": ""
    }
    return render(request, 'Home.html', Content)


def content(request):
    Content = {
        "home": "active",
        "about": "",
        "contact": ""
    }
    return render(request, 'Content.html', Content)
