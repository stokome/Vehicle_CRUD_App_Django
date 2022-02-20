from gc import get_objects
from inspect import Attribute
from re import template
from django.shortcuts import render
from django.views import generic
from .models import Vehicle
from django.http import HttpResponse, JsonResponse


class VehicleList(generic.ListView):
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'
    def get_queryset(self):
        return Vehicle.objects.order_by('-vehicle_number')

class VehicleDetail(generic.DetailView):
    model = Vehicle
    template_mame = 'vehicle_detail.html'
  
    # override context data
    
class VehicleCreate(generic.edit.CreateView):
    model = Vehicle
    fields = '__all__'
    template_name = 'vehicle_create.html'
    success_url = '/'

class VehicleUpdate(generic.edit.UpdateView):
    model = Vehicle
    model = Vehicle
    fields = '__all__'
    template_name = 'vehicle_update.html'
    success_url = '/'
    pk_url_kwarg = 'pk'
    
    
class VehicleDelete(generic.edit.DeleteView):
    model = Vehicle
    success_url = '/'
    pk_url_kwarg = 'pk'

