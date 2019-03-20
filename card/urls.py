from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('list_student/',views.List_student.as_view(),name='list_student'),
    path('list_employee/',views.List_employee.as_view(),name='list_employee'),
    path('detail/<pk>',views.Detail_student.as_view(),name='detail_student'),
    path('detail_employee/<pk>',views.Detail_employee.as_view(),name='detail_employee'),
    path('new_student/',views.New_student.as_view(),name='new_student'),
    path('new_employee/',views.New_employee.as_view(),name='new_employee'),
    path('update/<pk>',views.Update_student.as_view(),name='update_student'),
    path('update_employee/<pk>',views.Update_employee.as_view(),name='update_employee'),
    path('delete_student/<pk>',views.Delete_student.as_view(),name='delete_student'),
    path('delete_employee/<pk>',views.Delete_employee.as_view(),name='delete_employee'),
    path('print/<pk>', views.GeneratePdf.as_view(),name='print'),
    path('print_employee/<pk>', views.GeneratePdf_employee.as_view(),name='print_employee'),
    path('barcode/<bar_id>', views.barcode,name='barcode'),
    path('add_new/', views.add_new,name='add_new'),
]
