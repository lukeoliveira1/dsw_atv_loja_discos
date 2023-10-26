from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from core.forms import DiskForm

from core.models import Disk

def list_disks(request):
    disks = Disk.objects.all()
    return render(request, 'index.html', {'disks': disks})

def detail_disk(request, disk_id):
    disk = get_object_or_404(Disk, pk=disk_id)
    return render(request, 'detail_disk.html', {'disk': disk})

def create_disk(request):
    context = {'acao': 'Cadastrar'}
    if request.method == "POST":
        form = DiskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:list-disks'))
        else:
            context['form'] = form
            return render(request, 'disks/form_disk.html', context)
    else:
        context['form'] = DiskForm()
        return render(request, 'disks/form_disk.html', context)
    
def edit_disk(request, disk_id):
    context = {'acao': 'Editar'}
    if request.POST:
        form = DiskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('core:list-disks'))
        else:
            context['form'] = form
            return render(request, 'disks/form_disk.html', context)
    else:
        disk = Disk.objects.get(pk=disk_id)
        form = DiskForm(instance=disk)
        context['form'] = form

        return render(request, 'disks/form_disk.html', context)
    
def delete_disk(request, disk_id):
    disk = Disk.objects.get(pk=disk_id)
    disk.delete()
    return HttpResponseRedirect(reverse('core:list-disks'))