from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .full_model import full_model

# Create your views here.

def index(request):
    return render(
        request,
        'nasdaq/nasdaq.html',
        {
            'ndq': full_model()
        }
    )
