from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    chenna = Product.objects.all()
    return render(request, 'index.html', {'sony': chenna})


def travel(request):
    return HttpResponse(' live a life you will remember')
