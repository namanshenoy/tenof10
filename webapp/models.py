from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class SystemOverview(models.Model):
  serial = models.IntegerField(default=0)
  company = models.CharField(max_length=255, blank=True, null=True)
  model = models.CharField(max_length=255, blank=True, null=True)
  updated_date = models.DateTimeField(default=datetime.now())
  installed_date = models.DateTimeField(default=datetime.now())
  storage_capacity = models.DecimalField(max_digits=15, decimal_places=10)
  storage_free_pct = models.DecimalField(max_digits=15, decimal_places=10)
  storage_capacity_fc = models.DecimalField(max_digits=15, decimal_places=10)
  storage_capacity_nl = models.DecimalField(max_digits=15, decimal_places=10)
  storage_capacity_ssd = models.DecimalField(max_digits=15, decimal_places=10)
  dedupe_ratio = models.DecimalField(max_digits=15, decimal_places=10)
  tdvv_count = models.IntegerField(default=0)
  tdvv_capacity = models.DecimalField(max_digits=15, decimal_places=10)
  