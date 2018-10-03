from django.forms import ModelForm
from django.forms.widgets import TextInput

from .models import Area


class AreaForm(ModelForm):

    class Meta:
        model = Area
        fields = ['nome', 'cor', 'icone', 'prioridade']
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }
