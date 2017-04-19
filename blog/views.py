from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

# Create your views here.

def index(request):
    entries = Entry.objects.all()
    context = {
        'entries':entries,
    }
    return render(request, 'index.html', context)

def entries(request,id):
    entry = Entry.objects.filter(identifier=id)
    context = {
        'entry':entry,
    }
    return render(request,'entry.html',context)
