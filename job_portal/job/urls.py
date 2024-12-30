from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_job, name="create-job"),
    path("delete/<int:job_id>/", views.delete_job, name="delete-job"),
    path("update/<int:job_id>/", views.update_job, name="update-job"),
    path("", views.list_job, name="list-jobs")
]
