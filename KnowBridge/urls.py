from django.urls import path
from .views import upload_syllabus

urlpatterns = [
    path('upload_syllabus/', upload_syllabus, name='upload_syllabus'),
    # Add more paths for different views
]
