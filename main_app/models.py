from datetime import date
from django.db import models

class Status(models.Model):
    nome = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
    

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    data_termino = models.DateField(default=date.today)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, 
                                related_name='status', to_field='id', default='1') 
    
    def __str__(self):
        return self.titulo