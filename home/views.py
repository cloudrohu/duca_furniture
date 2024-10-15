from django.shortcuts import render
from home.models import *


# Create your views here.
def index(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    slider = Slider.objects.all().order_by('-id')[0:1]
    
    

    page="home"
    context={
        'setting':setting,
        'slider':slider,
    }

    return render(request,'main/index.html',context)

