from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from main_app.forms import TarefaForm
from main_app.models import Status, Tarefa

def create_item(request):
    # Lista de todas as tarefas e status disponíveis
    tarefas = Tarefa.objects.all()
    status_list = Status.objects.all()

    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a nova tarefa
            return redirect('/')  # Redireciona para a página inicial
        
    form = TarefaForm()
    context = {"form": form, 'tarefas': tarefas, 'status_list': status_list}
    return render(request, 'index.html', context)

def delete_item(request):
    tarefa_id = request.GET.get('tarefa_id')  # Obtém o ID da tarefa a ser deletada
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()  # Deleta a tarefa do banco de dados
    data = {'status': 'delete'}
    return JsonResponse(data)

def update_item(request):
    data_id = request.GET.get('data_id')  # Obtém o ID da tarefa a ser atualizada
    titulo = request.GET.get('titulo')  # Obtém o novo título para a tarefa

    tarefa = get_object_or_404(Tarefa, id=data_id)  # Obtém a tarefa pelo ID
    tarefa.titulo = titulo  # Atualiza o título da tarefa
    tarefa.save()  # Salva a tarefa atualizada no banco de dados

    data = {'status': 'update-item', 'titulo': titulo}
    return JsonResponse(data)

def update_status(request):
    data_id = request.GET.get('data_id')  # Obtém o ID da tarefa cujo status será atualizado
    status_id = request.GET.get('status_id')  # Obtém o ID do novo status para a tarefa
    
    status = Status.objects.get(id=status_id)  # Obtém o objeto do novo status pelo ID
    
    tarefa = get_object_or_404(Tarefa, id=data_id)  # Obtém a tarefa pelo ID
    tarefa.status = status  # Atualiza o status da tarefa
    tarefa.save()  # Salva a tarefa atualizada no banco de dados
    
    data = {'status': status_id}
    return JsonResponse(data)
