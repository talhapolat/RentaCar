from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    text = "sellammm"
    context = {'tete': text}
    return render(request, 'index.html', context)