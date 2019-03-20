import random,string
from django.db import models
from django.utils import timezone
from django.urls import reverse
from reportlab.lib.units import mm
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from . import mybarcode
import os


class Card_detail(models.Model):
    roll_no=models.CharField(max_length=256,primary_key=True)
    name=models.CharField(max_length=256)
    father_name=models.CharField(max_length=256)
    dob=models.DateField()
    programme=models.CharField(max_length=256)
    blood_group=models.CharField(max_length=256)
    issued_on=models.DateField()
    valid_upto=models.DateField()
    pic = models.ImageField(upload_to = 'images/',null=True,verbose_name="")

    def __str__(self):
        return self.roll_no
    class Meta:
        ordering = ["roll_no"]

    def get_absolute_url(self):
        mybarcode.MyBarcodeDrawing(self.roll_no).save(formats=['png'],outDir=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'media/barcodes/'),fnRoot=self.roll_no) 
        return reverse('list_student')

ID_LENGTH = 4
def create_unique_id():
    return ''.join(random.choices(string.digits, k=ID_LENGTH))
def id_gen()-> str:
    idd = create_unique_id()
    unique = False
    while not unique:
        if not idd in Employee_Card.objects.filter(e_id=id).values_list('e_id', flat=True):
            unique = True
        else:
            idd = create_unique_id()
    mybarcode.MyBarcodeDrawing(idd).save(formats=['png'],outDir=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'media/barcodes/'),fnRoot=idd)
    return idd



class Employee_Card(models.Model):

    e_id = models.CharField(max_length=ID_LENGTH, primary_key=True, default=id_gen, editable=False)
    name=models.CharField(max_length=256)
    designation=models.CharField(max_length=256)
    dob=models.DateField()
    blood_group=models.CharField(max_length=256)
    pic = models.ImageField(upload_to = 'images/',null=True,verbose_name="")
    valid_upto=models.DateField()
    issued_on=models.DateField(null=True)

    def __str__(self):
        return self.e_id
    # class Meta:
    #     ordering = ["e_id"]

    def get_absolute_url(self):
        return reverse('list_employee')


