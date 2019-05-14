from django.shortcuts import render, get_object_or_404
from .models import Event, Meeting, MeetingMinutes, Resource
from .forms import MeetingForm, ResourceForm

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getResources(request):
    resources_list=Resource.objects.all()
    context={'resources_list' : resources_list}
    return render(request, 'clubapp/resources.html', context=context)

def resourceDetails(request, id):
    resce=get_object_or_404(Resource, pk=id)
    context = {
        'resce' : resce,
    }
    return render(request, 'clubapp/resourcedetails.html', context=context)

def getMeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'clubapp/meetings.html', {'meeting_list' : meeting_list})

def meetingDetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context = {
        'meet' : meet,
    }
    return render(request, 'clubapp/meetingdetails.html', context=context)

def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save
            form=MeetingForm()
    else:
        form=MeetingForm()

    return render(request, 'clubapp/newmeeting.html', { 'form' : form })

def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save
            form=ResourceForm()
    else:
        form=ResourceForm()

    return render(request, 'clubapp/newresource.html', { 'form' : form })