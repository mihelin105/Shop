from django.shortcuts import render
from django.http import HttpResponse

# /products -> call the index function
def index(request):
    return HttpResponse("You're at the index.")

def new(request):
    return HttpResponse("New clothing.")