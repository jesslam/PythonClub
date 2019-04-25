from django.shortcuts import render
from .models import Event, Meeting, MeetingMinutes, Resource

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getResources(request):
    resources_list=Resource.objects.all()
    context={'resources_list' : resources_list}
    return render(request, 'clubapp/resources.html', context=context)
