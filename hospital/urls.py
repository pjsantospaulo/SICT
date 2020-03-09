from django.urls import path

from hospital.views import HospitalCreateView, HospitalListView

urlpatterns = [
    path('create/', HospitalCreateView.as_view(), name='hospital_create'),
    path('list/', HospitalListView.as_view(), name='hospital_list'),
]
