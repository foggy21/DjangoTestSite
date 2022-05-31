from django.shortcuts import render
from django.http import HttpResponse


def index(request): #Функция принимает экзампляр класса httpRequest. Там хранятся все данные о пользователе, куки-шмуки и т.д
    #print(dir(request))
    return HttpResponse('Hello World!')

def test(reques):
    return HttpResponse('<h1>Tested Page :)</h1>')