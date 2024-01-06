from django.shortcuts import render
from django.http import HttpResponse
from .models import Voltage, Current, Power, test

# Create your views here.
def index(request):
    Voltage1 = Voltage.objects.all()
    Current1 = Current.objects.all()
    Power1   = Power.objects.all()
    test1= test.objects.all()
    return render(request, 'index.html', {'Voltage':Voltage1, 'Current':Current1, 'Power':Power1, 'test':test1})

def trend(request):
    return render(request, 'trend.html')
