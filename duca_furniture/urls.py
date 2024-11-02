from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import home
from home import views 
from django.contrib.auth.views import LoginView,LogoutView

from django.utils.translation import gettext_lazy as _

from django.views.generic import RedirectView



urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),



    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path(('about/'), views.aboutus, name='aboutus'),
    path(('contactus/'), views.contactus, name='contactus'),
    path(('faqs/'), views.faqs, name='faqs'),


    path(('product/'), views.product, name='product'),
    path('product_details/<slug:slug>', views.product_details, name='product_details'),
    path('product/filter-data',views.filter_data,name="filter-data"),
    
    path(('brand/'), views.BRAND, name='brand'),
    path(('category-list/'), views.category_list, name='category-list'),

    path(('blog/'), views.BLOG, name='blog'),
    path('404', views.error404, name='404'),

    path('accounts/', include('django.contrib.auth.urls')),
    
    path('account/my_account', views.my_account, name='my_account'),
    path('accounts/register', views.register, name='handleregister'),
    path('accounts/login', views.LOGIN, name='handlelogin'),
    path('account/profile', views.PROFILE, name='profile'),
    path('account/profile/update', views.PROFILE_UPDATE, name='profile_update'),
    path('logout/', views.logout_user, name='logout'),





    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
