from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(PurchaseOrder)
admin.site.register(Vendor)
admin.site.register(HistoricalPerformance)