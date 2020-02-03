from django.urls import path

from hospital.views import hospital_new

urlpatterns = [
    path('new/', hospital_new, name='hospital_new'),
]
