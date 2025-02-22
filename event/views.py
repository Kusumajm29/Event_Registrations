from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Registration
from .forms import RegistrationForm

class RegistrationCreateView(CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'events/register.html'
    success_url = reverse_lazy('registration_success')

class RegistrationListView(ListView):
    model = Registration
    template_name = 'events/registrations_list.html'
    context_object_name = 'registrations'

# Create your views here.
