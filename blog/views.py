from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. "my_blog" from source code.
def my_blog(request):
    return HttpResponse("Hello Blog!")
