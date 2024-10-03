from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  
    path("form/", views.feedbackForm, name="form"),  
    path("dashboard/", views.dashboard, name="dashboard"), 
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('success/', views.success_view, name='success'),   
]