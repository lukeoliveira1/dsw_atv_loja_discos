from django.urls import path
from core.views import list_disks, detail_disk, create_disk, edit_disk

app_name = "core"

urlpatterns = [
    path('', list_disks, name='list-disks'),
    path('create-disk', create_disk, name='create-disk'),
    path('edit-disk/<int:disk_id>', edit_disk, name="edit-disk"),
    path('disk/<int:disk_id>/', detail_disk, name='detail-disk'),
]