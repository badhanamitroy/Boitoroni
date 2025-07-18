from django.urls import path
from . import views

urlpatterns = [
    path('PDFStorage/', views.PDFStorage, name='PDFStorage'),
]