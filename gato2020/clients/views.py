from django.shortcuts import render, redirect
from .models import ImportantClient
from .forms import ImportantClientForm

def important_clients_list(request):
    clients = ImportantClient.objects.all()
    return render(request, 'clients/important_clients.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        form = ImportantClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('important_clients_list')
    else:
        form = ImportantClientForm()
    return render(request, 'add_client.html', {'form': form})
