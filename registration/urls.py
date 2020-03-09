from django.urls import path

from registration.views import RegistrationCreateView, RegistrationListView

urlpatterns = [
    path('create/', RegistrationCreateView.as_view(), name='registration_new'),
    path('list/', RegistrationListView.as_view(), name='registration_list')
]
