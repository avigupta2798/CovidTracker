from django.db import models

# Create your models here.

class Covid(models.Model):
    patient_number = models.AutoField(primary_key=True) 
    age = models.IntegerField(null=True, blank=True)
    backup_notes = models.TextField(null=True, blank=True)
    current_status = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50,null=True, blank=True)   
    gender = models.CharField(max_length=1, null=True, blank=True)  # M/F
    nationality = models.CharField(max_length=50, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    source1 = models.URLField(max_length=500, null=True, blank=True)
    source2 = models.URLField(max_length=500, null=True, blank=True)
    source3 = models.URLField(max_length=500, null=True, blank=True)
    statecode = models.CharField(max_length=5, null=True, blank=True)
    status_change_date = models.DateTimeField(null=True, blank=True)
    type_of_transmission = models.CharField(max_length=50,null=True, blank=True)