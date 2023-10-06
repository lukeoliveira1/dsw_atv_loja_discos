from django.contrib import admin

from core.models import Disk, Artist, PhonographicSeal

# Register your models here.
admin.site.register(Disk)
admin.site.register(Artist)
admin.site.register(PhonographicSeal)