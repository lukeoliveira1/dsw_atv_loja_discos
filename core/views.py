from django.shortcuts import get_object_or_404, render

from core.models import Disk

# Create your views here.
def list_disks(request):
    disks = Disk.objects.all()
    return render(request, 'index.html', {'disks': disks})

def detail_disk(request, disk_id):
    disk = get_object_or_404(Disk, pk=disk_id)
    return render(request, 'detail_disk.html', {'disk': disk})