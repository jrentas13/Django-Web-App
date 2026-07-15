from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm


def homepage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            full_message = f"""
            You received a message from your portfolio website.

            Name:
            {name}

            Email:
            {email}

            Message:
            {message}
            """

            try:
                send_mail(
                    subject,
                    full_message,
                    email,
                    ["javy.rentas@gmail.com"],
                )
                submitted = True

            except Exception as e:
                print(e)
                submitted = False
                

            form = ContactForm()

            submitted = True

        else:
            submitted = False
        
    else:
        form = ContactForm()
        submitted = False
    

    projects = [
        {
            "title": "Calorie Tracker",
            "description": ("A Django web app that helps users track calories and meals."),
            "tools": ["Python", "Django", "HTML", "CSS", "JavaScript"],
            "image": "folio/images/calorie-tracker.png",
            "github_url": "https://github.com/abitsma/Health_App",
            "live_url": ""
        },
        {
            "title": "Portfolio Website",
            "description": ("A personal portfolio website built with Django"),
            "tools": ["Python", "Django", "Bootstrap"],
            "image": "folio/images/portfolio.png",
            "github_url": "https://github.com/jrentas13/Django-Web-App",
            "live_url": ""
        },
        {
            "title": "Starving College Students",
            "description": ("A recipe sharing website designed to provide delicious and affordable"
            "recipes to college students."),
            "tools": ["JavaScript", "Node.js", "HTML", "CSS", "MySQL"],
            "image": "folio/images/starving-college-students.png",
            "github_url": "https://github.com/jrentas13/Starving-College-Students",
            "live_url": ""
        }
    ]

    context = {
        "name": "Javier Rentas",
        "title": "Computer Engineer",
        "introduction": ("I'm a Computer Engineering building projects to broaden my skillset"
        "in web development."),
        "projects": projects,
        "form": form,
        "submitted": submitted,
    }

    return render(request, "folio/homepage.html", context)