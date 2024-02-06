from django.http import HttpResponse
from django.shortcuts import render

def hello_notes(request):
    return HttpResponse("Hello from Notes app.")
