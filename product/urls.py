from django.urls import path

from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('addcomment/<int:id>', views.AddComment, name='addcomment'),
    path('makeorder/', views.MakeOrder, name='makeorder'),

]