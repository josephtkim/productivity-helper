from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from todos.models import Todo
from goals.models import Goal
from journal.models import Entry
from django.utils import timezone

# Create your views here.
def signup(request):
    if request.method == "POST":
        if not request.POST['email'] or not request.POST['username'] or not request.POST['password1']: # Check if email field empty
            return render(request, 'accounts/signup.html', {'error': 'Cannot leave fields blank'})

        if request.POST['password1'] == request.POST['password2']:
            # Check that email is not already taken
            try:
                profile = User.objects.get(email=request.POST['email'])
                return render(request, 'accounts/signup.html', {'error': 'Email has already been taken'})
            except:
                pass

            # Check that username is not already taken
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                login(request, user)

                # If successful sign up, create a profile
                profile = Profile()
                profile.user = request.user
                profile.save()

                # Add examples to profile
                # Example todo
                todo = Todo()
                todo.title = "Groceries"
                todo.pub_date = timezone.now()
                todo.author = request.user
                todo.point_value = 10
                todo.completed = False
                todo.save()

                todo2 = Todo()
                todo2.title = "Add a new Task!"
                todo2.pub_date = timezone.now()
                todo2.author = request.user
                todo2.point_value = 10
                todo2.completed = False
                todo2.save()

                todo3 = Todo()
                todo3.title = "Clean room"
                todo3.pub_date = timezone.now()
                todo3.author = request.user
                todo3.point_value = 10
                todo3.completed = False
                todo3.save()

                # Example Goals
                goal = Goal()
                goal.title = "Study"
                goal.amount_goal = 10
                goal.units = "hours"
                goal.amount_per_increment = 1
                goal.point_value = 25
                goal.pub_date = timezone.now()
                goal.author = request.user
                goal.current_amount_done = 0
                goal.times_completed = 0
                goal.save()

                goal2 = Goal()
                goal2.title = "Jogging"
                goal2.amount_goal = 30
                goal2.units = "miles"
                goal2.amount_per_increment = 1
                goal2.point_value = 30
                goal2.pub_date = timezone.now()
                goal2.author = request.user
                goal2.current_amount_done = 0
                goal2.times_completed = 0
                goal2.save()

                goal2 = Goal()
                goal2.title = "Pull-ups"
                goal2.amount_goal = 100
                goal2.units = "reps"
                goal2.amount_per_increment = 20
                goal2.point_value = 15
                goal2.pub_date = timezone.now()
                goal2.author = request.user
                goal2.current_amount_done = 0
                goal2.times_completed = 0
                goal2.save()

                # Example journal entry
                entry = Entry()
                entry.title = "Hello world!"
                entry.content = "Welcome to the Productivity Helper app! This is an example Journal entry, which you are free to edit or delete."
                entry.author = request.user
                entry.published_date = timezone.now()
                entry.save()

                return redirect('todos:home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords did not match'})
    else:
        return render(request, 'accounts/signup.html')

def loginview(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('todos:home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username and password do not match'})
    else:
        return render(request, 'accounts/login.html')

def logoutview(request):
    if request.method == "POST":
        logout(request)
        return redirect('todos:home')

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})
