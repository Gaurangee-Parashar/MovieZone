from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from social.models import Review
from .models import Profile
from .forms import CreateUserForm
# Create your views here.

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password isn\'t correct.')
    context = {}
    return render(request, 'user_management/Login.html', context)

def logoutView(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            profile = Profile.objects.create(
                user=user
            )
            profile.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during the registration process')

    return render(request, 'user_management/Register.html', {'form' : form})

def profile(request, id):
    user = User.objects.get(id=id)
    profile = user.profile
    liked_movies = user.profile.likedmovie_set.all()
    reviews = Review.objects.filter(user=user)
    context = {'user' : user, 'liked_movies' : liked_movies, 'profile' : profile, 'reviews' : reviews}
    return render(request, 'user_management/profile.html', context)