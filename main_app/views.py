from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from main_app.forms import TarefaForm
from main_app.models import Status, Tarefa

def create_item(request):
    tarefas = Tarefa.objects.all() # Query com todos objetos da lista
    status_list = Status.objects.all()

    if request.method == "POST": # para POST
        form = TarefaForm(request.POST)  
        if form.is_valid():
            form.save() # salva informação
            return redirect('/')
        
    form = TarefaForm() # Formulário
    context = {"form" : form, 'tarefas': tarefas, 'status_list': status_list}
    return render(request, 'index.html', context)

def delete_item(request):
    tarefa_id  = request.GET.get('tarefa_id') # Id da Lista
    tarefa = Tarefa.objects.get(id = tarefa_id) # Pega Objeto
    tarefa.delete() # Deleta
    data = {'status':'delete'}
    return JsonResponse(data)

def update_item(request):  
    data_id  = request.GET.get('data_id') # Id da Lista
    titulo = request.GET.get('titulo') # Id do status
    print(data_id, titulo)

    tarefa = get_object_or_404(Tarefa, id=data_id) # Get Objeto lista
    tarefa.titulo = titulo # status recebe novo valor "Id do status"
    tarefa.save() # salva  

    data = {'status':'update-item', 'titulo':titulo}
    return JsonResponse(data) # retorna

def update_status(request):  
    data_id  = request.GET.get('data_id') # Id da Lista
    status_id = request.GET.get('status_id') # Id do status 
    
    status = Status.objects.get(id = status_id) # Get objeto status 
    
    tarefa = get_object_or_404(Tarefa, id = data_id) # Get Objeto lista
    tarefa.status = status # status recebe novo valor "Id do status"
    tarefa.save() # salva  
    
    data = {'status': status_id}
    return JsonResponse(data)