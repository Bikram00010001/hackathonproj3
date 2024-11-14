from django.contrib import admin
from .models import crop ,fertilizer,Biopesticide,Herbicide,Openprice,Govprice,states
# Register your models here.

admin.site.register(crop)
admin.site.register(fertilizer)
admin.site.register(Biopesticide)
admin.site.register(Herbicide)
admin.site.register(Openprice)
admin.site.register(Govprice)
admin.site.register(states)