from django.shortcuts import render,HttpResponse,redirect
from .models import NewsPost
#pylint: disable=unused-argument

def home(request):
    top_news_carousel=NewsPost.objects.all()[0:3]
    top_news_grid=NewsPost.objects.all()[3:7]
    context = {'top_news_carousel':top_news_carousel,'top_news_grid':top_news_grid}



    return render(request,'reporterKidiary/index.html',context)
