from django.shortcuts import render
from .models import Entry


def home(request):
    home_entries = Entry.objects.filter(hide=False).order_by('creation_date')
    context = {
        'entries': home_entries,
    }
    return render(request, 'home.html', context)


def entries(request, entry_id):
    entry = Entry.objects.get(identifier=entry_id)
    context = {
        'entry': entry,
        'entry_file': entry.get_file(),
    }
    return render(request, 'entry.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)
