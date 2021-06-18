from django.shortcuts import render
from .models import Telebashniya1, Foydalanuvchi, Galereya, Restourant, Foods

def index(request):
    print('meals')
    if request.POST:
        print(request.POST)
        bashni = Telebashniya1()
        bashni.title = request.POST.get('index1')
        bashni.text = request.POST.get('index2')
        bashni.save()
    return render(request, 'index.html')


def about(request):
    print('meals')
    if request.POST:
        print(request.POST)
        about = Foydalanuvchi()
        about.name = request.POST.get('abaut1')
        about.email = request.POST.get('abaut2')
        about.number = request.POST.get('abaut3')
        about.manzili = request.POST.get('abaut4')
        about.save()
    return render(request, 'about.html')



def map(request):
    print('meals')
    if request.POST:
        print(request.POST)
        news = Foods()
        news.foods = request.POST.get('map1')
        news.Ichimliklar = request.POST.get('map2')
        news.salatlar = request.POST.get('map3')
        news.shirinliklar = request.POST.get('map4')
        news.save()
    return render(request, 'map.html')




def meals(request):
    print('meals')
    if request.POST:
        mealss = Restourant()
        mealss.ism = request.POST.get('meals1')
        mealss.telefon_raqam = request.POST.get('meals2')
        mealss.odamlar_soni = request.POST.get('meals3')
        mealss.sana = request.POST.get('meals4')
        mealss.save()
    return render(request, 'meals.html')



def news(request):
    if request.POST:
        print(request.POST)
        news = Galereya()
        news.title = request.POST.get('first_name')
        news.save()
    return render(request, 'new.html')





