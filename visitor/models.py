from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime

class visitor_detail(models.Model):
    name=models.CharField(max_length=256)
    name_2=models.CharField(max_length=256)
    address=models.CharField(max_length=256)
    id_no=models.CharField(max_length=256)
    id_type=models.CharField(max_length=256)
    mob=models.CharField(max_length=256)
    email=models.CharField(max_length=256)
    veh=models.CharField(max_length=256)
    purpose=models.CharField(max_length=256)
    dest=models.CharField(max_length=256)
    time_in=models.DateTimeField(default=datetime.now, blank=True)
    status_in=models.BooleanField(default=True)
    time_out=models.DateTimeField(default=datetime.now, blank=True)
    #pic = models.ImageField(upload_to = 'images/',null=True,verbose_name="")
    pic=models.CharField(max_length=100000)

    def __str__(self):
        return self.name
