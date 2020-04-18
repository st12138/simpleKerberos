from django.urls import path
from django.http import HttpResponse,JsonResponse
from . import views
def index(request):

    response = HttpResponse("Hello, world. You're at the action .You can get your tgt or sgt by url action/gettgt and action/getsgt")
    return response
urlpatterns = [
    path('',index,name='index'),
    path('gettgt/', views.gettgt, name='gettgt'),
    path('getsgt/', views.getsgt, name='getsgt'),
    path('connect/',views.connect,name='connect'),
]