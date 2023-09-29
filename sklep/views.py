from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from sklep.models import Meeting
def welcome(request):
    return render(request, "index.html",{"a":Meeting.objects.count(),"b": "khug"})
def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))
def dwa(request):

    return HttpResponse("lubie spac")