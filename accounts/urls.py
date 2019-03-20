from django.urls import path
from . import views
import card

urlpatterns = [
    path('signup/',views.SignupView.as_view(),name='signup' ),
    path('profile/',card.views.index,name='index' ),

]