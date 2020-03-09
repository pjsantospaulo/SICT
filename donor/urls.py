from django.urls import path

from donor.views import DonorCreateView, DonorListView

urlpatterns = [
    path('create/', DonorCreateView.as_view(), name='donor_create'),
    path('list/', DonorListView.as_view(), name='donor_list'),
]

