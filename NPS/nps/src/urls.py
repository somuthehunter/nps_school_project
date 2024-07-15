from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',student_payment,name='student-payment' ),
    path('payment_status/',payment_status,name='student-status' ),
]