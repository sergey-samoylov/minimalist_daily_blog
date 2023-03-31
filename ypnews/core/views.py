import datetime

from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.shortcuts import redirect, render

from story.models import Story
from .forms import CreateUserForm

def index(request):
    today = datetime.date.today()
    stories = Story.objects.filter(created_at__gte=today).order_by('-number_of_votes')[0:50]

    if request.user.is_authenticated:
        for story in stories:
            story.has_voted = False

            if story.votes.filter(created_by=request.user):
                story.has_voted = True

    context = {
        'stories': stories,
    }
    return render(request, 'core/index.html', context)

def new(request):
    today = datetime.date.today()
    stories = Story.objects.filter(created_at__gte=today).order_by('-created_at')

    if request.user.is_authenticated:
        for story in stories:
            story.has_voted = False

            if story.votes.filter(created_by=request.user):
                story.has_voted = True

    context = {
        'stories': stories,
    }
    return render(request, 'core/new.html', context)

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'core/signup.html', context)
