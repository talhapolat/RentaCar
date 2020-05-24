from django.urls import path

from . import  views

urlpatterns = [
    path('', views.account, name='index'),
    path('orders', views.orders, name='orders'),
    path('comments', views.comments, name='comments')

]