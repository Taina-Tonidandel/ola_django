from django.urls import path
from.import views
from django.http import HttpResponse

def oiDjango(request):
    return HttpResponse('Olá primeiroAPP')

urlpatterns = [
    path('OlaApp/', oiDjango)
]