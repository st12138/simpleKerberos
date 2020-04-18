from django.urls import path

from . import views

urlpatterns = [
    path('givetgt/', views.givetgt, name='gettgt'),
    path('givesgt/', views.givesgt, name='getsgt'),
]