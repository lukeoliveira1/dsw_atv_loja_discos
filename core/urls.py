from django.urls import path
from core.views import list_disks, detail_disk

app_name = "core"

urlpatterns = [
    path('', list_disks, name='list-disks'),
    path('disk/<int:disk_id>/', detail_disk, name='detail-disk'),
]