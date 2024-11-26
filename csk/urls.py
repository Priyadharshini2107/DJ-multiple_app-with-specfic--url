from django.contrib import admin
from django.urls import path
from csk.views import*

urlpatterns=[
    path('admin/',admin.site.urls),
    path('captain/',captain,name='captain'),
    path('Dhoni/',Dhoni,name='Dhoni'),
]