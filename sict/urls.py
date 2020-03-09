
from django.contrib import admin
from django.urls import include
from django.urls import path

from hospital import urls as hospital_urls
from registration import urls as registration_urls
from donor import urls as donor_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hospital/', include(hospital_urls)),
    path('registration/', include(registration_urls)),
    path('donor/', include(donor_urls)),

]
