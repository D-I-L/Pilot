# Create your views here.
from django.shortcuts import render


def index(request):
    msg = "Hello, world. You're at the site index"
    context = {'msg': msg, 'TITLE': "Django and Bootstrap"}
    return render(request, 'HelloWorld/index.html', context)