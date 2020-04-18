from django.urls import path

from . import views
def index(request):
    response = HttpResponse("Hello, world. You're at the action .You can get your connect by url action/connect")
    return response
urlpatterns = [
    path('',index,name='index'),
    path('connect/', views.connect, name='connect'),
]