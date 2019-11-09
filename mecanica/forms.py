from django import forms

from .models import Auto, Trabajo, Mecanico

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ( 'nombre_propietario', 'placas', 'modelo', 'anio')

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ( 'auto_placas', 'trabajo_descripcion', 'costo_total', 'estado', 'mecanicos')

    def __init__ (self, *args, **kwargs):
        super(TrabajoForm, self).__init__(*args, **kwargs)
        self.fields["mecanicos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["mecanicos"].help_text = "Ingrese los mecanicos que trabajaran en el vehiculo"
        self.fields["mecanicos"].queryset = Mecanico.objects.all()
