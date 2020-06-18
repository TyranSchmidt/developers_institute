from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .form import ProfileForm
from .models import Profile, Card
from Card_Game_App.models import Pokemon
import random

# Create your views here.

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('create_profile')
    return render(request, 'Register.html', {
        'form': form
    })

def home(request):
    count = User.objects.count()
    return render(request, 'Home.html', {
        'count': count
    })

@login_required
def create_profile(request):
    if Profile.objects.filter(user=request.user).exists():
        return redirect('profile')
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            random_cards(request)
            return redirect('profile')
    return render(request, 'Create_Profile.html', {
        'form':form
        })

@login_required
def profile(request):
    if not Profile.objects.filter(user=request.user).exists():
        return redirect('create_profile')
    return render(request, 'Profile.html')

@login_required
def card_collection(request):
    return render(request, 'Card_Collection.html')


def random_cards(request):
    for x in range(0, 5):
        pokemon = random.choice(Pokemon.objects.all())
        card = Card.objects.create(pokemon=pokemon, profile=request.user.profile)
