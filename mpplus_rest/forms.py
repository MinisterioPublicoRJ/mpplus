from django import forms

from .models import Area, Tema, Icone
# from .scrapper import tableau_data


class IconeForm(forms.ModelForm):
    class Meta:
        model: Icone
        fields = ['nome', 'data_file']


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome', 'cor', 'icone', 'prioridade']


class TableauWidget(forms.widgets.Select):
    def __init__(self, attrs=None):
        super().__init__(attrs)


class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = '__all__'
        # widgets = {
        #     'url_tableau': forms.Select(
        #         choices=tableau_data(profile='mprj', count=200)
        #     )
        # }
