from django.shortcuts import render


def Home(req):
    return render(req,'home.html',{})
