from .views import base,home,contact,gallery,login,registration
from django.urls import path

urlpatterns=[
    path('ba/',base),
    path('ho/',home),
    path('co/',contact),
    path('ga/',gallery),
    path('lo/',login),
    path('re/', registration)
]