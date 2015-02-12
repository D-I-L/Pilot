from django.http.response import HttpResponse


# Create your views here.
def welcome(request):
    '''
    Display the welcome message.
    '''
    return HttpResponse("Welcome to My First Django Project !!! !")


def read_and_render(request):
    '''
    Read the file and render its content
    '''
    return HttpResponse("Going to read the file !  File contents : " + read_file())


def read_file():
    '''
    function to read file
    '''
    filepath='/gdxbase/www/prem-dev/github-playground/Pilot'
    with open('/gdxbase/www/prem-dev/github-playground/Pilot/pilot') as a_file:
        return a_file.read()
    