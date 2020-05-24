from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting
from product.models import CommentForm, Comment, Category, Product, Office, Order


def index(request):
    return HttpResponse('Product Sayfası')


def AddComment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #current_user = request.user
            data = Comment()
            data.user = form.cleaned_data['user']
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.email = form.cleaned_data['email']
            data.comment = form.cleaned_data['comment']
            data.product_id = id
            data.status = 'NEW'
            #data.user_id = current_user
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz gönderildi.")
            url = request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(url)

    return HttpResponse("Gönderilemedi..")



def MakeOrder(request):
    data = Order()
    data.product = Product.objects.get(id=request.GET['vehicleid'])
    data.user = request.user
    data.startdate = datetime.strptime(request.GET['startdate'], "%d/%m/%Y").date()
    data.enddate = datetime.strptime(request.GET['enddate'], "%d/%m/%Y").date()
    data.vehicletype = request.GET['vehicletype']
    data.office = Office.objects.get(id=request.GET['office'])
    data.status = request.GET['status']
    data.endhour= request.GET['endhour']
    data.starthour = request.GET['starthour']
    data.rentdays = abs((data.startdate - data.enddate).days)
    data.price = data.rentdays * data.product.price
    data.days = abs((data.startdate - data.enddate).days)
    data.create_at = datetime.now()
    data.save()
    messages.success(request, "Yorumunuz gönderildi.")
    return HttpResponseRedirect('/account/orders')