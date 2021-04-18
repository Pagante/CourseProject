from django.urls import path
from . import views

urlpatterns = [
    path('Allcourse',views.courseDetail, name='Allcourse'),
]