from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Goal
from .forms import GoalForm
from accounts.models import Profile

from django.utils import timezone

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    goals = Goal.objects.filter(author=request.user).filter(is_completed=False).order_by('-pub_date')
    completed_goals = Goal.objects.filter(author=request.user).filter(is_completed=True).order_by('-pub_date')
    return render(request, 'goals/index.html', {'goals': goals, 'completed_goals': completed_goals})

@login_required
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['target_goal'] and request.POST['units']:
            goal = Goal()
            goal.title = request.POST['title']
            goal.amount_goal = request.POST['target_goal']
            goal.units = request.POST['units']

            goal.amount_per_increment = 1
            goal.point_value = 25
            goal.pub_date = timezone.now()
            goal.author = request.user
            goal.current_amount_done = 0
            goal.times_completed = 0

            goal.save()

        return redirect('goals:home')
    else:
        goals = Goal.objects.filter(author=request.user).order_by('-pub_date')
        return render(request, 'goals/index.html', {'goals': goals})

def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    return render(request, 'goals/goal_detail.html', {'goal': goal})

def goal_edit(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.author = request.user
            goal.pub_date = timezone.now()
            goal.save()
            return redirect('goals:home')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'goals/goal_edit.html', {'form': form})

def increment_goal(request, pk):
    if request.method == "POST":
        goal = get_object_or_404(Goal, pk=pk)
        exp_points = goal.increment()
        goal.save()

        # Add exp points to user profile
        profile = Profile.objects.get(user=request.user)
        profile.gain_exp(exp_points)
        profile.save()

        return redirect('goals:home')

def reset_goal(request, pk):
    if request.method == "POST":
        goal = get_object_or_404(Goal, pk=pk)
        goal.reset_progress()
        goal.save()
        return redirect('goals:home')

def delete_goal(request, pk):
    if request.method == "POST":
        goal = get_object_or_404(Goal, pk=pk)
        goal.delete()
        return redirect('goals:home')
