from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin

# Create your views here.
class CarListView(FormMixin, ListView):
    model = Car
    paginate_by = 15
    form_class = CarForm

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = CarForm(self.request.GET)
        if self.form.is_valid():
            filters = Car.get_filter(self.request.GET)
            return queryset.filter(filters)
        else:
            return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = self.form
        return context
