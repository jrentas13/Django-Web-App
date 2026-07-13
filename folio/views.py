from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    projects = [
        {
            "title": "Calorie Tracker",
            "description": ("A Django web app that helps users track calories and meals."),
            "tools": ["Python", "Django", "HTML", "CSS", "JavaScript"],
            "github_url": "https://github.com/abitsma/Health_App",
            "live_url": ""
        },
        {
            "title": "Portfolio Website",
            "description": ("A personal portfolio website built with Django"),
            "tools": ["Python", "Django", "Bootstrap"],
            "github_url": "https://github.com/jrentas13/Django-Web-App",
            "live_url": ""
        },
        {
            "title": "Starving College Students",
            "description": ("A recipe sharing website designed to provide delicious and affordable"
            "recipes to college students."),
            "tools": ["JavaScript", "Node.js", "HTML", "CSS", "MySQL"],
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
    }

    return render(request, "folio/homepage.html", context)