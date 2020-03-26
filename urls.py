from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('home/',views.home,name="home"),
    path('yazi/',views.yaziEkle, name="yazi"),
    path('yaziGonder/',views.yaziGonder,name="yaziGonder"),
    path('yazilar/',views.yazilar,name="yazılar")

]