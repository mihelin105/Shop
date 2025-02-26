from django.urls import path
from . import views

# '' root of an app, passing a reference of the function
urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
]
