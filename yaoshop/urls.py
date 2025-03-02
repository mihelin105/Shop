from products import views
from django.contrib import admin
from django.urls import path, include
from register import views as views_register

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')), # any view function is stored here
    path("register/", views_register.register, name='register'),

]
