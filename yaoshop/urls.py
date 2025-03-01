from products import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')), # any view function is stored here

]
