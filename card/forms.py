from django import forms
import datetime
from .models import Card_detail,Employee_Card


class DateInput(forms.DateInput):
   input_type = 'date'

class Card_detail_form(forms.ModelForm):
   # roll_no = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Roll Number','class':'form-control'}))
   # name=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}))
   # father_name=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Father\'s Name','class':'form-control'}))
   # dob=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Date of Birth','class':'form-control','id':'datepicker1'}))
   # programme=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Programme','class':'form-control'}))
   # blood_group=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Blood Group','class':'form-control'}))
   # valid_upto=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Valid Upto','class':'form-control','id':'datepicker'}))
   # issued_on=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'issued_on','class':'form-control','id':'datepicker2'}))
   # #pic=forms.CharField(label="",widget=forms.FileInput(attrs={'name':'pic'}))
  
   class Meta():
       model=Card_detail
       fields='__all__'
       widgets={
       'roll_no':forms.TextInput(attrs={'placeholder':'Roll Number','class':'form-control'}),
       'name':forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
       'father_name':forms.TextInput(attrs={'placeholder':'Father\'s Name','class':'form-control'}),
       'dob':forms.TextInput(attrs={'placeholder':'Date of Birth','class':'form-control','id':'datepicker1'}),
       'programme':forms.TextInput(attrs={'placeholder':'Programme','class':'form-control'}),
       'blood_group':forms.TextInput(attrs={'placeholder':'Blood Group','class':'form-control'}),
       'valid_upto':forms.TextInput(attrs={'placeholder':'Valid Upto','class':'form-control','id':'datepicker'}),
       'issued_on':forms.TextInput(attrs={'placeholder':'issued_on','class':'form-control','id':'datepicker2'}),
       # 'pic':forms.FileInput(attrs={'name':'pic','paceholder':'Photo','class':'form-control'}),'roll_no':forms.TextInput(attrs={'placeholder':'Roll Number'}),
       # 'name':forms.TextInput(attrs={'placeholder':'Name'}),
       # 'father_name':forms.TextInput(attrs={'placeholder':'Father\'s Name'}),
       # 'dob':DateInput(attrs={'placeholder':'Date of Birth'}),
       # 'programme':forms.TextInput(attrs={'placeholder':'Programme'}),
       # 'blood_group':forms.TextInput(attrs={'placeholder':'Blood Group'}),
       # 'valid_upto':DateInput(attrs={'placeholder':'Valid Upto'}),
       # 'issued_on':DateInput(attrs={'placeholder':'issued_on'}),
       'pic':forms.FileInput(attrs={'name':'pic','paceholder':'Photo','class':'form-control'}),

       }


class Employee_card_form(forms.ModelForm):
  # name=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}))
  # designation=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Designation','class':'form-control'}))
  # dob=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Date of Birth','class':'form-control','id':'datepicker1'}))
  # blood_group=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Blood Group','class':'form-control'}))
  # # pic=forms.CharField(label="",widget=forms.FileInput(attrs={'name':'pic'}))
  # valid_upto=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Valid Upto','class':'form-control','id':'datepicker1'}))
  class Meta():
    model=Employee_Card
    fields='__all__'
    widgets={
    'name':forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
    'designation':forms.TextInput(attrs={'placeholder':'Designation','class':'form-control'}),
    'dob':forms.TextInput(attrs={'placeholder':'Date of Birth','class':'form-control','id':'datepicker1'}),
    'blood_group':forms.TextInput(attrs={'placeholder':'Blood Group','class':'form-control'}),
    'pic':forms.FileInput(attrs={'name':'pic','class':'form-control','placeholder':'Photo'}),
    'valid_upto':forms.TextInput(attrs={'placeholder':'Valid Upto','class':'form-control','id':'datepicker'}),           
    'issued_on':forms.TextInput(attrs={'placeholder':'Issued on','class':'form-control','id':'datepicker2'}),           
    }