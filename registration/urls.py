from django.urls import path

from registration.views import registration_new

urlpatterns = [
    path('', registration_new, name='registration_new')
]