from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
from django.utils import timezone
from .models import Post
import random

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {})



def randomizer_en(request):
    url1 = "https://google.com"
    url2 = "https://wikipedia.org"
    url3 = "https://twitter.com"
    url4 = ""

    url_list = [url1, url2, url3, url4]

    return redirect(random.choice(url_list))

def randomizer_es(request):
    url1 = "https://google.com"
    url2 = "https://wikipedia.org"
    url3 = "https://twitter.com"

    url_list = [url1, url2, url3, url4]

    return redirect(random.choice(url_list))

def randomizer_it(request):
    url1 = "https://google.com"
    url2 = "https://wikipedia.org"
    url3 = "https://twitter.com"

    url_list = [url1, url2, url3, url4]

    return redirect(random.choice(url_list))


def button(request):
    return render(request,'home.html')

