from django.shortcuts import render
from .models import Entry

import markdown


def home(request):
    home_entries = Entry.objects.order_by('creation_date')
    context = {
        'entries': home_entries,
    }
    return render(request, 'home.html', context)


def entries(request, entry_id):
    entry = Entry.objects.get(identifier=entry_id)
    entry_text = markdown.markdown(entry.get_text())
    context = {
        'entry': entry,
        'entry_text': entry_text,
    }
    return render(request, 'entry.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)
