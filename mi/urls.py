from django.contrib import admin
from django.urls import path
from mi.views import*

urlpatterns=[
    path('admin/',admin.site.urls),
    path('captain/',captain,name='captain'),
    path('vicecaptain/',vicecaptain,name='vicecaptain'),
]