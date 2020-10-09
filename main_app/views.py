from django.shortcuts import render
from .models import Activity
from django.views.generic import ListView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def facts(request):
  return render(request, 'facts.html')

class ActivityList(ListView):
    model = Activity