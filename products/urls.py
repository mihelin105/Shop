from django.contrib import admin
from django.urls import path, include
from . import views

# '' root of an app, passing a reference of the function
urlpatterns = [
    path('', views.index, name='index'),  # home
    path('new', views.new, name='new'),
    path('decors/<str:category_name>/', views.decor_category, name='decor_category'),  # Dynamic category filter,
    path('admin/', admin.site.urls),
]
