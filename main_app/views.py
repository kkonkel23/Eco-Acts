from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'home.html')

def facts(request):
  return render(request, 'facts.html')