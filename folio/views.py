from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    projects = [
        {
            "title": "Calorie Tracker",
            "description": "A Django web app that helps users track calories and meals.",
            "tools": "Python, Django, HTML, CSSS, JavaScript",
            "link": "#"
        },
        {
            "title": "Portfolio Website",
            "description": "A personal portfolio website built with Django",
            "tools": "Python, Django, Bootstrap",
            "link": "#",
        },
    ]

    context = {
        "name": "Javier Rentas",
        "title": "Computer Engineer",
        "projects": projects,
    }

    return render(request, "folio/homepage.html", context)