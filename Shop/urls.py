from django.contrib import admin
from django.urls import path
from shop import views  # Імпортуємо в'юхи саме з нового додатка shop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
]