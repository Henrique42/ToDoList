from django import forms
from .models import Tarefa

class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)

class TarefaForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Título:")
    data_termino = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), label="Término:")

    class Meta:
        model = Tarefa
        fields = ['titulo', 'data_termino']