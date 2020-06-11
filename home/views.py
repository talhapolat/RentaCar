from datetime import datetime, timedelta
import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from home.forms import SignUpForm, SearchForm
from home.models import Setting, ContactForm, Contact, UserProfile
from product.models import Product, Category, Office, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    offices = Office.objects.all()
    context = {'setting': setting, 'page': 'home', 'sliderdata': sliderdata, 'category': category, 'offices': offices}
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()  # model baglantısı
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm()
    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'contact.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'aboutus', 'category': category}
    return render(request, 'aboutus.html', context)


def login_view(request):
    if request.method == 'POST' and request.POST['formtype'] == 'signin':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Giriş Başarısız')
            return HttpResponseRedirect('/login')

    if request.method == 'POST' and request.POST['formtype'] == 'signup':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/user.png"
            data.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Kayıt yapılamadı')
            return HttpResponseRedirect('/login')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = SignUpForm()
    context = {'setting': setting, 'page': 'aboutus', 'category': category, 'form': form}
    return render(request, 'login.html', context)


def logout_view(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'aboutus', 'category': category}
    logout(request)
    return HttpResponseRedirect('/login')


def products(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products = Product.objects.all()
    context = {'setting': setting, 'page': 'cars', 'category': category, 'products': products}
    return render(request, 'products.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            setting = Setting.objects.get(pk=1)
            category = Category.objects.all()
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            context = {'setting': setting, 'page': 'cars', 'category': category, 'products': products}
            return render(request, 'products.html', context)


def account(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,'category': category}
    return render(request, 'account.html', context)


def get_places(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = Product.objects.filter(title__icontains=q)
        results = []
        for pl in places:
            place_json = {}
            place_json = pl.title
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def productdetail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='TRUE')
    context = {'setting': setting, 'page': 'cars', 'category': category, 'slug': slug, 'product': product,
               'images': images, 'comments': comments}
    return render(request, 'productpage.html', context)


def category(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    category_active = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'setting': setting, 'page': 'cars', 'category': category, 'products': products, 'slug': slug,
               'main_category': category_active}
    return render(request, 'categorypage.html', context)


def check(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    startdate = datetime.strptime(request.GET['startdate'], "%m/%d/%Y").date()
    enddate = datetime.strptime(request.GET['enddate'], "%m/%d/%Y").date()
    vehicletype = request.GET['vehicletype']
    products = Product.objects.filter(category_id=vehicletype)
    office = Office.objects.get(id=request.GET['office'])
    starthour = request.GET['starthour']
    endhour = request.GET['endhour']

    context = {'setting': setting, 'page': 'cars', 'category': category, 'products': products, 'startdate': startdate,
               'enddate': enddate, 'vehicletype': vehicletype, 'office': office, 'starthour': starthour,
               'endhour': endhour}
    return render(request, 'check.html', context)


def checkend(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product = Product.objects.get(id=request.GET['vehicleid'])
    startdate = datetime.strptime(request.GET['startdate'], "%d/%m/%Y").date()
    enddate = datetime.strptime(request.GET['enddate'], "%d/%m/%Y").date()
    vehicletype = request.GET['vehicletype']
    office = Office.objects.get(id=request.GET['office'])
    starthour = request.GET['starthour']
    endhour = request.GET['endhour']
    rentdays = abs((startdate - enddate).days)
    totalprice = rentdays * product.price

    context = {'setting': setting, 'page': 'cars', 'category': category, 'product': product,
               'startdate': startdate, 'enddate': enddate, 'vehicletype': vehicletype, 'office': office,
               'starthour': starthour, 'endhour': endhour, 'rentdays': rentdays, 'totalprice': totalprice}
    return render(request, 'checkend.html', context)


def AddEndDays(request, id):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product = Product.objects.get(id=request.GET['vehicleid'])
    startdate = datetime.strptime(request.GET['startdate'], "%d/%m/%Y").date()
    enddate = datetime.strptime(request.GET['enddate'], "%d/%m/%Y").date()
    vehicletype = request.GET['vehicletype']
    office = Office.objects.get(id=request.GET['office'])
    starthour = request.GET['starthour']
    endhour = request.GET['endhour']
    rentdays = abs((startdate - enddate).days)

    if (id == 1 and rentdays > 1):
        enddate -= timedelta(days=1)
        rentdays -= 1
    if (id == 2):
        enddate += timedelta(days=1)
        rentdays += 1

    totalprice = rentdays * product.price

    context = {'setting': setting, 'page': 'cars', 'category': category, 'product': product,
               'startdate': startdate, 'enddate': enddate, 'vehicletype': vehicletype, 'office': office,
               'starthour': starthour, 'endhour': endhour, 'rentdays': rentdays, 'totalprice': totalprice}
    return render(request, 'checkend.html', context)


def AddStartDays(request, id):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products = Product.objects.all()
    startdate = datetime.strptime(request.GET['startdate'], "%d/%m/%Y").date()
    enddate = datetime.strptime(request.GET['enddate'], "%d/%m/%Y").date()
    vehicletype = request.GET['vehicletype']
    office = Office.objects.get(id=request.GET['office'])
    starthour = request.GET['starthour']
    endhour = request.GET['endhour']

    if (id == 1):
        startdate -= timedelta(days=1)
    if (id == 2):
        startdate += timedelta(days=1)

    context = {'setting': setting, 'page': 'cars', 'category': category, 'products': products,
               'startdate': startdate, 'enddate': enddate, 'vehicletype': vehicletype, 'office': office,
               'starthour': starthour, 'endhour': endhour}
    return render(request, 'check.html', context)
