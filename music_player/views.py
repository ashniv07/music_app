from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Song
from django.contrib.auth.decorators import login_required

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
def about_us_view(request):
    # Add any necessary logic here
    return render(request, 'about_us.html')