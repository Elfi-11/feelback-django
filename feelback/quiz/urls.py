from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form/", views.feedbackForm, name="form"),
    path("dashboard/", views.dashboard, name="dashboard"),
]