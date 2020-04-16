from django.db import models

# Create your models here.

class Covid(models.Model):
    patient_number = models.AutoField(primary_key=True) 
    age = models.CharField(max_length=10, null=True, blank=True, default='')
    backup_notes = models.TextField(null=True, blank=True, default='')
    current_status = models.CharField(max_length=50, null=True, blank=True, default='')
    date_announced = models.TextField(max_length=50, null=True, blank=True, default='')
    city = models.CharField(max_length=50, null=True, blank=True, default='')
    district = models.CharField(max_length=50, null=True, blank=True, default='')
    state = models.CharField(max_length=50,null=True, blank=True, default='')   
    gender = models.CharField(max_length=1, null=True, blank=True, default='')  # M/F
    nationality = models.CharField(max_length=50, null=True, blank=True,default='')
    notes = models.TextField(null=True, blank=True, default='')
    source1 = models.URLField(max_length=500, null=True, blank=True, default='')
    source2 = models.URLField(max_length=500, null=True, blank=True, default='')
    source3 = models.URLField(max_length=500, null=True, blank=True, default='')
    statecode = models.CharField(max_length=5, null=True, blank=True, default='')
    status_change_date = models.TextField(max_length=50, null=True, blank=True, default='')
    type_of_transmission = models.CharField(max_length=50,null=True, blank=True, default='')