from django.urls import path
from . import views
from telebashniya_uzb.views import index, about, meals, news
from .views import map

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("map/", views.map, name="map"),
    path("meals/", views.meals, name="meals"),
    path("news/", views.news, name="news"),
]