from django.urls import path
from .views import *


# Create your tests here.

urlpatterns = [

    path('dadosPaciente/', buscarDados , name = 'dadosPaciente'),
    path('cadastroPaciente/', cadastrarPaciente , name = 'cadastrarPaciente'),

  ]
