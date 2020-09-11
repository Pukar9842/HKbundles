from typing import Tuple

from django.contrib import admin
from . models import FundFarm




class FundFarmAdmin(admin.ModelAdmin):
    list_display = ('crop_name', 'cost_per_unit', 'units_available', 'roi_in_percent', 'tenure_for_ROI')
admin.site.register(FundFarm, FundFarmAdmin)
