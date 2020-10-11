from django.shortcuts import render
from .models import Activity, MyActivity
from django.views.generic import ListView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def facts(request):
  return render(request, 'facts.html')

# def my_activites_index(request, activity_id):
#     activity = Activity.objects.get(id=activity_id)
#     activities_user_doesnt_have = Activity.objects.exclude(id__in = activity.myactivity.all().values_list('id'))
#     return render(request, 'my_activity_index.html', {
#         'activity': activity, 'activities': activities_user_doesnt_have
#     })

def assoc_activity(request, activity_id, myactivity_id):
  Activity.objects.get(id=activity_id).myactivity.add(myactivity_id)
  return redirect('my_activities_index', activity_id=activity_id)

class ActivityList(ListView):
    model = Activity

class MyActivityList(ListView):
    model = MyActivity

