from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name ="homeurl"),
    path('about/', views.about, name ="abouturl"),

]