from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import Template, Context


# Create your views here.
def welcome(request):
    '''
    Display the welcome message.
    '''
    return HttpResponse("Welcome to My First Django Project !!! !")


def greet(request):
    '''
    Display the greeting page.
    '''
    msg = "hello world"
    context = {'greet': msg}
    return render(request, 'helloworld.html', context)


def read_and_render(request):
    '''
    Read the file and render its content
    '''
    return HttpResponse("Going to read the file !  File contents : " + read_file()) 


def read_file():
    '''
    function to read file
    '''
    filepath='/gdxbase/www/prem-dev/github-playground/Pilot/pilot'
    with open(filepath) as a_file:
        return a_file.read()
    