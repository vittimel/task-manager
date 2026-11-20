from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.
def lista_tarefas(request):
    filtro = request.GET.get('status', None)
    if filtro == 'concluidas':
        tarefas = Tarefa.objects.filter(concluida=True).order_by("criada_em")
    elif filtro == 'pendentes':
        tarefas = Tarefa.objects.filter(concluida=False).order_by("criada_em")
    else:
        tarefas = Tarefa.objects.order_by("criada_em")

    contexto = {
        "tarefas": tarefas,
        "status": filtro,
        "total": Tarefa.objects.count(),
        "pendentes": Tarefa.objects.filter(concluida=False).count(),
        "concluidas": Tarefa.objects.filter(concluida=True).count(),
    }
    return render(request, "lista.html", contexto)

def nova_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tarefas")
    else:
        form = TarefaForm()

    return render(
        request, "nova.html",
        {"form": form}
    )
    return render(request,"nova.html")

def detalhe_tarefa(request,pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(
        request, "detalhes.html",
        {"tarefa": tarefa}
    )
    return render(request,"detalhes.html")

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == "POST":
        form = TarefaForm(
            request.POST, instance=tarefa
        )
        if form.is_valid():
            form.save()
            return redirect(
                "detalhe_tarefa", pk=tarefa.pk
            )
    else:
        form = TarefaForm(instance=tarefa)

    return render(
        request, "tarefa_form.html",
        {"form": form, "tarefa": tarefa}
    )

def excluir(request,pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == "POST":
        tarefa.delete()
        return redirect("lista_tarefas")

    return render(
        request, "confirmar_exclusao.html",
        {"tarefa": tarefa}
    )

def alternar(request,pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if request.method == "POST":
        tarefa.concluida = not tarefa.concluida
        tarefa.save()
        #form = TarefaForm(request.POST, instance=tarefa)
        return redirect("detalhe_tarefa", pk=tarefa.pk)
            
    return render(
        request, "confirmar_alternar.html",
        {"tarefa": tarefa}
    )
    return render(request,"detalhes.html")