from django.db import models

class FundFarm(models.Model):
    crop_name = models.CharField(max_length=255)
    cost_per_unit = models.FloatField(max_length=10)
    units_available = models.IntegerField()
    image_url = models.CharField(max_length=2084)
    roi_in_percent = models.IntegerField()
    tenure_for_ROI = models.IntegerField()


