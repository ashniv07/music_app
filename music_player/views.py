from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Song
from django.contrib.auth.decorators import login_required

from .models import Song, UserProfile

from django.shortcuts import get_object_or_404



@login_required
def index(request):
    query = request.GET.get('q')
    songs = Song.objects.all()
    if query:
        songs = songs.filter(title__icontains=query) | songs.filter(artist__icontains=query)
    return render(request, 'index.html', {'songs': songs, 'query': query})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def add_to_watch_later(request, song_name):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        song = get_object_or_404(Song, title=song_name)
        user_profile.watch_later.add(song)
        return redirect('watch_later')  
    else:
        return redirect('login')  
@login_required
def remove_from_watch_later(request, title):
    user_profile = UserProfile.objects.get(user=request.user)
    song = Song.objects.get(title=title)
    user_profile.watch_later.remove(song)
    return redirect('index')

def watch_later(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        watch_later_songs = user_profile.watch_later.all()
        return render(request, 'watch_later.html', {'watch_later_songs': watch_later_songs})
    else:
        return redirect('login')
    
def about_us_view(request):
  
    return render(request, 'about_us.html')
 