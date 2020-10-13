from django.shortcuts import render, redirect
from .models import Activity, MyActivity, User, Note
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import NoteForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def facts(request):
  return render(request, 'facts.html')

def blog(request):
    return render(request, 'blog.html')


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      MyActivity(user_id = user.id).save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def user_activities(request, user_id):
  user = User.objects.get(id=user_id)
  my_activities = MyActivity.objects.get(user_id=user_id).my_activities.all()
  context = {
    'user': user,
    'my_activities': my_activities,
  }
  note_form = NoteForm()
  return render(request, 'user_activities.html',{ 'note_form': note_form, 'user': user,'my_activities': my_activities,})

@login_required
def assoc_activity(request, activity_id, user_id):
    activity = Activity.objects.get(id=activity_id)
    MyActivity.objects.get(user_id=user_id).my_activities.add(activity)
    return redirect('user_activities', user_id)

@login_required
def unassoc_activity(request, activity_id, user_id):
    activity = Activity.objects.get(id=activity_id)
    MyActivity.objects.get(user_id=user_id).my_activities.remove(activity)
    return redirect('user_activities', user_id)

class ActivityList(LoginRequiredMixin,ListView):
    model = Activity

@login_required
def activities_detail(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    if request.user.username:
        user_activities = MyActivity.objects.get(user_id=request.user.id).my_activities.all()
    else:
        user_activities = {}
    context = {
        'activity': activity,
        'user_activities': user_activities,
    }
    return render(request, 'main_app/activity_detail.html', context)

@login_required
def add_note(request, user_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.user_id = user_id
        new_note.save()
    return redirect('user_activities', user_id=user_id)

class NoteDelete(LoginRequiredMixin,DeleteView):
    model = Note
    success_url = '/activities/'

class NoteUpdate(LoginRequiredMixin,UpdateView):
    model = Note
    fields = ['name', 'content']
    success_url = '/activities/'