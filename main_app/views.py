from django.shortcuts import redirect, render

from main_app.forms import TarefaForm
from main_app.models import Tarefa

def create_item(request):
    todo = Tarefa.objects.all() # Query com todos objetos da lista
    if request.method == "POST": # para POST
        form = TarefaForm(request.POST)  
        if form.is_valid():
            form.save() # salva informação
            return redirect('/')
        
    form = TarefaForm() # Formulário
    context = {"form" : form, 'todo': todo}
    return render(request, 'index.html', context)

def delete_item(request, id):
    todo = Tarefa.objects.get(id=id) # pega o objeto
    todo.delete() # deleta
    return redirect('/')