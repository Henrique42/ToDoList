from django import forms 
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('titulo',)
        exclude = ('status',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
                field.widget.attrs['class'] = 'form-control'