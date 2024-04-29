from django.shortcuts import render
#from django.http import HttpResponse
from .models import Article

# Create your views here.
def home(request):
    context = {
        "articles" : Article.objects.filter(status='p').order_by('-publish')#[:3]
    }
    return render(request,"blog/home.html", context)

def detail (request, slug):
    context = {
        "articles" : Article.objects.get(slug = slug)

    }
    return render(request,"blog/single.html", context)
