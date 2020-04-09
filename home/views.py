from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from home.models import Setting, ContactForm, Contact
from product.models import Product, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'home', 'sliderdata': sliderdata, 'category': category}
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()   #model baglantısı
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'setting': setting, 'form': form}
    return render(request, 'contact.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'aboutus'}
    return render(request, 'aboutus.html', context)