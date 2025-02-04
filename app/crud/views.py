from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from core.models import Cliente
from .forms import ClientForm
from django.contrib.auth import logout

# Create your views here.


class CreateClientView(CreateView):
    model = Cliente
    form_class = ClientForm
    template_name = "clientes/formclientes.html"
    success_url = reverse_lazy('crud:list_client')


class ListClientView(ListView):
    model = Cliente
    template_name = "clientes/listclientes.html"
    context_object_name = "clientes"


class UpdateClientView(UpdateView):
    model = Cliente
    form_class = ClientForm
    template_name = "clientes/formclientes.html"
    success_url = reverse_lazy('crud:list_client')


class DeleteClientView(DeleteView):
    model = Cliente
    template_name = "clientes/deleteclientes.html"
    success_url = reverse_lazy('crud:list_client')


def logout_view(request):
    logout(request)
    return redirect('registration:signin')
