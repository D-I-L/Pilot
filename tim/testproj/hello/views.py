from django.shortcuts import render


def greet(request):
    '''
    Display the greeting page.
    '''
    msg = "hello"
    context = {'greet': msg}
    return render(request, 'hello/greet.html', context)
