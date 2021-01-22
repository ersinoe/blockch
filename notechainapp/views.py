from django.shortcuts import render

def home(request):
    return render(request, "notechainapp/home.html")

def about(request):
    context = {"title": "About"}
    return render(request, "notechainapp/about.html", context)
