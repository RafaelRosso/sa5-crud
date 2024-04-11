from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('atualizar/<int:id>',views.atualizar, name='atualizar'),
    path('deletar/<int:id>',views.deletar, name='deletar'),
]