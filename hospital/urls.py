from django.urls import path

from hospital.views import hospital_new, hospital_create

urlpatterns = [
    path('new/', hospital_new, name='hospital_new'),
    path('create/', hospital_create, name='hospital_create'),
]
