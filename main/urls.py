from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('other/', views.second_page, name='other_page'),
]