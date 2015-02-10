from django.shortcuts import render

def greet(request):
    msg = "hello"
    context = {'greet': msg}
    return render(request, 'hello/greet.html', context)

