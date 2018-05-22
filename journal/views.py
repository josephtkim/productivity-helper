from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm

from django.utils import timezone

# Create your views here.
@login_required
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['content']:
            entry = Entry()
            entry.title = request.POST['title']
            entry.content = request.POST['content']
            entry.author = request.user
            entry.published_date = timezone.now()
            entry.save()
            return redirect('journal:home')
        else:
            return render(request, 'journal/entry_new.html', {'error': 'Cannot leave fields blank'})
    else:
        entries = Entry.objects.order_by('-published_date').filter(author=request.user)
        return render(request, 'journal/index.html', {'entries': entries})

@login_required(login_url='/accounts/login/')
def home(request):
    entries = Entry.objects.order_by('-published_date').filter(author=request.user)
    return render(request, 'journal/index.html', {'entries': entries})

def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if entry.author != request.user:
        return redirect('journal:home')

    return render(request, 'journal/entry_detail.html', {'entry': entry})

def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if entry.author != request.user:
        return redirect('journal:home')

    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.published_date = timezone.now()
            entry.save()
            return redirect('journal:home')
    else:
        form = EntryForm(instance=entry)
    return render(request, 'journal/entry_edit.html', {'form': form})

def entry_new(request):
    return render(request, 'journal/entry_new.html')

def entry_delete(request, pk):
    if request.method == "POST":
        entry = get_object_or_404(Entry, pk=pk)
        if entry.author != request.user:
            return redirect('journal:home')

        entry.delete()
        return redirect('journal:home')
