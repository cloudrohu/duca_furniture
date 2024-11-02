from django.shortcuts import render,redirect
from home.models import *
from product.models import *
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.views import LoginView,LogoutView

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

def filter_data(request):
    sub_category = request.GET.getlist('sub_category[]')
    brands = request.GET.getlist('brand[]')

    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(sub_category) > 0:
        allProducts = allProducts.filter(sub_category__id__in=sub_category).distinct()

    if len(brands) > 0:
        allProducts = allProducts.filter(Brand__id__in=brands).distinct()


    t = render_to_string('ajax/product.html', {'product': allProducts})

    return JsonResponse({'data': t})

def error404(request):     
     
    return render(request, 'main/404.html')


def logout_user(request):     
    logout (request)
    return redirect('/')


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

        if User.objects.filter(username = username).exists():
            messages.error(request,'Username is already exists')
            return redirect('login')
        
        if User.objects.filter(email= email).exists():
            messages.error(request,'email id alredy exists')
            return redirect('login')

        user = User(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()    
    return redirect('login',)


def LOGIN(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Email Id & Passwors invalid")
            return redirect('login',) 



@login_required(login_url='/accounts/login/')
def PROFILE(request):     
     
    return render(request, 'account/profile.html')



@login_required(login_url='/accounts/login/')
def PROFILE_UPDATE(request):    
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email =email
    
        if password != None and password != "":
            user.set_password(password)
        user.save()
     
    return redirect('profile')

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