from django.urls import path
from . import views
urlpatterns = [
# indicando qual o metodo sera executado quando a home for chamada
path('', views.meu_html)
]