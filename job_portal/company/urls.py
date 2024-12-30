from django.urls import path
from . import views

urlpatterns = [
    path("create-company/", views.create_company, name="create-company"),
    path("", views.company_view, name="company-view"),
]
