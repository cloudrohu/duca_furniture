from django.shortcuts import render
from home.models import *
from product.models import *


# Create your views here.
def index(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    slider = Slider.objects.all().order_by('-id')[0:6]
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')
    
    

    page="home"
    context={
        'setting':setting,
        'slider':slider,
        'category':category,
        'sub_category':sub_category,
    }

    return render(request,'main/index.html',context)

def aboutus(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    slider = Slider.objects.all().order_by('-id')[0:6]
    
    

    page="home"
    context={
        'setting':setting,
        'slider':slider,
    }

    return render(request,'main/about.html',context)

def product(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    product = Product.objects.all().order_by('?')

    page="home"
    context={
        'setting':setting,
        'product':product,
    }
    return render(request,'main/product.html',context)

def faqs(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/FQA.html',context)

def contactus(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/contact.html',context)

def BRAND(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/BRAND.html',context)

def BLOG(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]

    page="home"
    context={
        'setting':setting,
    }
    return render(request,'main/BLOG.html',context)