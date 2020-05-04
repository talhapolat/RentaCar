"""firstp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('vehicle/', views.products, name='products'),
    path('product/', include('product.urls')),
    path('<slug:slug>/<int:id>/', views.productdetail, name='productdetail'),
    path('check/', views.check),
    path('checkend/', views.checkend),
    path('checkend/AddEndDays/<int:id>/', views.AddEndDays, name='adddays'),
    path('check/AddStartDays/<int:id>/', views.AddStartDays, name='adddays'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('<int:id>/<slug:slug>/', views.category, name='category'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
