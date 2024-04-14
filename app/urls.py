from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('criar/',views.criar, name='criar'),
    path('pesquisar/',views.pesquisar, name='pesquisar'),
    path('atualizar/<int:id>',views.atualizar, name='atualizar_id'),
    path('atualizar/',views.atualizar, name='atualizar'),
    path('deletar/<int:id>',views.deletar, name='deletar_id'),
    path('deletar/',views.deletar, name='deletar'),
]