from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def index(request):
    requested_path = request.path
    print(requested_path)
    if requested_path == '/':
        requested_path = 'intro.html'
        return render(request, requested_path)
    elif '.html' in requested_path: 
        html_file = open('Webpages/templates/' + requested_path, 'r')
        return HttpResponse(html_file.read())

# def index(request):
# 	return render(request, 'intro.html'))