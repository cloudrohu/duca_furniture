from django.shortcuts import render,redirect
from home.models import *
from product.models import *
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

from django.contrib.auth import authenticate,logout,login

# Create your views here.
def index(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    slider = Slider.objects.all().order_by('-id')[0:6]
    banner = Banner.objects.all().order_by('-id')[0:3]
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')
    
    

    page="home"
    context={
        'setting':setting,
        'slider':slider,
        'category':category,
        'sub_category':sub_category,
        'banner':banner,
    }

    return render(request,'main/index.html',context)

def aboutus(request):    
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
    return render(request,'main/about.html',context)

def category_list(request):    
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
    return render(request,'main/category_list.html',context)

def product(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    product = Product.objects.all().order_by('?')
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')
    
    

    page="home"
    context={
        'setting':setting,
        'product':product,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'main/product.html',context)


def product_details(request,slug): 
    setting = Setting.objects.all().order_by('-id')[0:1]
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')

    product = Product.objects.filter(slug = slug)
    if product.exists():
        product = Product.objects.get(slug = slug)
    else :
        return redirect('404')
    context = {

        'product': product,
        'setting': setting,
        'category':category,
        'sub_category':sub_category,
    }   
     
    return render(request, 'main/product_detail.html',context)


def error404(request):     
     
    return render(request, 'main/404.html')


def faqs(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')

    page="home"
    context={
        'setting':setting,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'main/FQA.html',context)

def my_account(request):     
    setting = Setting.objects.all().order_by('-id')[0:1]
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')

    page="home"
    context={
        'setting':setting,
        'category':category,
        'sub_category':sub_category,
    }
     
    return render(request, 'account/my_account.html',context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()    
    return redirect('my_account')


def login(request):
    setting = Setting.objects.all().order_by('-id')[0:1]
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')

    page="home"
    context={
        'setting':setting,
        'category':category,
        'sub_category':sub_category,
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Email Id & Passwors invalid")
            return redirect('my_account') 
    return render(request, 'account/my_account.html',context)

def contactus(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')

    page="home"
    context={
        'setting':setting,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'main/contact.html',context)

def BRAND(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')

    page="home"
    context={
        'setting':setting,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'main/BRAND.html',context)

def BLOG(request):    
    setting = Setting.objects.all().order_by('-id')[0:1]
    category = Category.objects.all().order_by('-id')
    sub_category = Sub_Category.objects.all().order_by('-id')

    page="home"
    context={
        'setting':setting,
        'category':category,
        'sub_category':sub_category,
    }
    return render(request,'main/BLOG.html',context)