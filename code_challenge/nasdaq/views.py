from django.shortcuts import render
#from django.http import HttpResponse
from .full_model import full_model
from .models import MostTraded

# Create your views here.

def index(request):
    return render(
        request,
        'nasdaq/nasdaq.html',
        {
            'ndq': full_model(),
            'most_traded': MostTraded.objects.all()
        }
    )
