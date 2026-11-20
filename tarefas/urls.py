from django.urls import path
from . import views

urlpatterns = [    
    path('tarefas/', views.lista_tarefas,name="lista_tarefas"),
    path('tarefas/<int:pk>/', views.detalhe_tarefa, name="detalhe_tarefa"),
    path('tarefas/nova/', views.nova_tarefa,name="nova_tarefa"),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa,name="editar_tarefa"),
    path('tarefas/<int:pk>/alternar/', views.alternar,name="alternar"),
    path('tarefas/<int:pk>/excluir/', views.excluir,name="excluir"),
    path('', views.lista_tarefas, name="inicio"),
    path('tarefas/', views.lista_tarefas, name="lista_tarefas"),

]
