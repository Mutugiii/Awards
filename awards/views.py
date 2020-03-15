from django.shortcuts import render, HttpResponse, loader

def index(request):
    '''Index View Function'''
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))