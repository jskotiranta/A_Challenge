from django.shortcuts import render
from django.http import HttpResponse
from .full_model import full_model
from .models import MostTraded

# Create your views here.

def index(request):
    return render(request, 'nasdaq/nasdaq.html')

def button(request):
    ndq = full_model()
    most_traded = MostTraded.objects.all()
    context = {'ndq': ndq, 'most_traded': most_traded}
    return render(request, 'nasdaq/database.html', context=context)

