import xml.etree.cElementTree as et

from django import forms

from .models import Area, Tema, Icone
# from .scrapper import tableau_data


class IconeForm(forms.ModelForm):
    image = forms.FileField()
    image_original = None

    class Meta:
        model: Icone
        fields = ['nome', 'image']

    def __init__(self, *args, **kwargs):
        super(IconeForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        if 'image' in kwargs:
            self.image_original = self.initial['image']

    def clean_image(self):
        file = self.files.get('image')
        if not file:
            if self.image_original:
                return self.image_original
            else:
                raise forms.ValidationError('Must provide a SVG icon')
        else:
            tag = None
            try:
                for event, el in et.iterparse(file, ('start',)):
                    tag = el.tag
                    break
            except et.ParseError:
                raise forms.ValidationError('Not a SVG file')

            if not tag == '{http://www.w3.org/2000/svg}svg':
                raise forms.ValidationError('Not a SVG file')

        file.seek(0)
        return file.read().decode()


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
