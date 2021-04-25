from django.urls import path
from . import views

urlpatterns = [
    path("", views.mentor_form, name="mentor_form"),
    path("success/", views.form_success, name="form_success")
]
