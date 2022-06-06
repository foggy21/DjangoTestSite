from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request): #Функция принимает экзампляр класса httpRequest. Там хранятся все данные о пользователе, куки-шмуки и т.д
    news = News.objects.all()
    return render(request, 'news/index.html', {'news':news, 'title': 'Список новостей'})
