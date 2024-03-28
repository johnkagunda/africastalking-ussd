# ussdprojo/urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import ussd# Importing the ussd_handler directly from views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ussd', ussd),  # Mapping the ussd_handler function to the /ussd URL
]
