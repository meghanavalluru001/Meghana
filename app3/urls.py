from django.urls import path
from app3 import views
app_name='app3'

urlpatterns = [
    path('s3/', views.hash,name='s3'),
]