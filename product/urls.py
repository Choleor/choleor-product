from django.urls import path, include
from . import views

urlpatterns = [
    path('init/', views.authenticate),
    path('final/')
]
