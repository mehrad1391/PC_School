from django.urls import path
from .views import *

urlpatterns = [
    path('Courses/', CoursesListApiView.as_view()),
    path('session/', SessionsListApiView.as_view()),    
]
