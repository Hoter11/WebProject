from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

# Create your views here.

def home(request):
    entries = Entry.objects.order_by('creation_date')
    context = {
        'entries':entries,
    }
    return render(request, 'home.html', context)

def entries(request,id):
    entry = Entry.objects.get(identifier=id)
    context = {
        'entry':entry,
    }
    return render(request,'entry.html',context)

def contact(request):
    context = {}
    return render(request,'contact.html',context)

def about(request):
    context = {}
    return render(request,'about.html',context)
