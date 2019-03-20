from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from card import forms,models
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
	return render(request,'card/index.html')

def add_new(request):
	return render(request,'card/add_new.html')

class List_student(LoginRequiredMixin,ListView):
	context_object_name='list'
	model=models.Card_detail
	template_name='card/list.html'

class List_employee(LoginRequiredMixin,ListView):
	context_object_name='list'
	model=models.Employee_Card
	template_name='card/list_employee.html'

class Detail_student(LoginRequiredMixin,DetailView):
	context_object_name='student_detail'
	model=models.Card_detail
	template_name='card/detail.html'

class Detail_employee(LoginRequiredMixin,DetailView):
	context_object_name='employee_detail'
	model=models.Employee_Card
	template_name='card/employee_detail.html'

class New_student(LoginRequiredMixin,CreateView):
	model=models.Card_detail
	template_name='card/new.html'
	form_class=forms.Card_detail_form

class New_employee(LoginRequiredMixin,CreateView):
	model=models.Employee_Card
	template_name='card/new_employee.html'
	form_class=forms.Employee_card_form

class Update_student(LoginRequiredMixin,UpdateView):
	form_class=forms.Card_detail_form
	model=models.Card_detail
	template_name='card/update.html'

class Update_employee(LoginRequiredMixin,UpdateView):
	form_class=forms.Employee_card_form
	model=models.Employee_Card
	template_name='card/update_employee.html'

class Delete_student(LoginRequiredMixin,DeleteView):
	model=models.Card_detail
	template_name='card/delete.html'
	success_url=reverse_lazy('list_student')

class Delete_employee(LoginRequiredMixin,DeleteView):
	model=models.Employee_Card
	template_name='card/delete.html'
	success_url=reverse_lazy('list_employee')

from django.http import HttpResponse
from django.views.generic import View
from utils import render_to_pdf #created in step 4

class GeneratePdf(View):
	def get(self, request, *args, **kwargs):
		primary=self.kwargs['pk']
		student=models.Card_detail.objects.get(pk=primary)
		data={'student':student}
		pdf = render_to_pdf('card/card.html', data)
		return HttpResponse(pdf, content_type='application/pdf')

class GeneratePdf_employee(View):
	def get(self, request, *args, **kwargs):
		primary=self.kwargs['pk']
		employee=models.Employee_Card.objects.get(pk=primary)
		data={'employee':employee}
		pdf = render_to_pdf('card/employee_card.html', data)
		return HttpResponse(pdf, content_type='application/pdf')

import os
from . import mybarcode
def barcode(request,bar_id):
    mybarcode.MyBarcodeDrawing(bar_id).save(formats=['png'],outDir=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'media/barcodes/'),fnRoot=bar_id)
    return HttpResponse('image printed')