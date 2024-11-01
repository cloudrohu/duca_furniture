from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import home
from home import views 
from django.utils.translation import gettext_lazy as _

from django.views.generic import RedirectView
urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('logout/',RedirectView.as_view(url = '/admin/logout/')),



    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path(('about/'), views.aboutus, name='aboutus'),
    path(('contactus/'), views.contactus, name='contactus'),
    path(('faqs/'), views.faqs, name='faqs'),


    path(('product/'), views.product, name='product'),
    path('product_details/<slug:slug>', views.product_details, name='product_details'),
    
    path(('brand/'), views.BRAND, name='brand'),
    path(('category-list/'), views.category_list, name='category-list'),

    path(('blog/'), views.BLOG, name='blog'),
    path('404', views.error404, name='404'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('account/my_account', views.my_account, name='my_account'),
    path('account/register', views.register, name='register'),
    path('account/login', views.login, name='login'),




    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
