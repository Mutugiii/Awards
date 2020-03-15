from django.shortcuts import render, HttpResponse

def index(request):
    '''Index View Function'''
    return HttpResponse('This is not a Test!!!')