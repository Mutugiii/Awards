from django.shortcuts import render, HttpResponse

def index(request):
    '''Welcome page/index view function'''

    return HttpResponse('This is the index page')
