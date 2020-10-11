from django.shortcuts import render, redirect
from .models import Activity, MyActivity
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
  return render(request, 'home.html')

def facts(request):
  return render(request, 'facts.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# def my_activites_index(request, activity_id):
#     activity = Activity.objects.get(id=activity_id)
#     activities_user_doesnt_have = Activity.objects.exclude(id__in = activity.myactivity.all().values_list('id'))
#     return render(request, 'my_activity_index.html', {
#         'activity': activity, 'activities': activities_user_doesnt_have
#     })

def assoc_activity(request, activity_id, myactivity_id):
  Activity.objects.get(id=activity_id).myactivity.add(myactivity_id)
  return redirect('my_activities_index', activity_id=activity_id)

class ActivityList(LoginRequiredMixin,ListView):
    model = Activity

class MyActivityList(LoginRequiredMixin,ListView):
    model = MyActivity

