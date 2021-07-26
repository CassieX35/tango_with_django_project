from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('',views.index, name='index'), #views.index() will be called
    path('about/',views.about, name='about'),
]