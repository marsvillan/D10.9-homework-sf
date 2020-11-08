from django import forms
from cars.models import Car
from colorfield.widgets import ColorWidget


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('manufacturer', 'model', 'issue_year', 'transmission', 'color')

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
