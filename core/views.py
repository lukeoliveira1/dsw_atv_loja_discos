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
    if request.method == "POST":
        form = DiskForm(request.POST)
        if form.is_valid():
            disk = Disk()
            disk.name = form.cleaned_data["name"]
            disk.description = form.cleaned_data["description"]
            disk.phonographic_seal = form.cleaned_data["phonographic_seal"]
            disk.year = form.cleaned_data["year"]
            disk.country = form.cleaned_data["country"]
            disk.gender = form.cleaned_data["gender"]
            disk.quantity = form.cleaned_data["quantity"]
            disk.save()
            return HttpResponseRedirect(reverse('core:list-disks'))
        else:
            return render(request, 'core/templates/form_create_disk.html', {'form': form})
    else:
        form = DiskForm()
        return render(request, 'form_create_disk.html', {'form': form})
    