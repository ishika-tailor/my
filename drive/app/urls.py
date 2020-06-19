from django.urls import  path
from . import views

urlpatterns= [

    path('',views.home,name='home'),
    path('add_form',views.add_form,name='add_form'),
]