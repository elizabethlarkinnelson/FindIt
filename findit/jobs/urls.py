from django.urls import path

from . import views

app_name = 'jobs'
urlpatterns = [
    # ex: /jobs/
    path('', views.all_jobs, name='all_jobs'),
    # ex: /jobs/1/
    path('<int:job_id>/', views.job_detail, name='job_detail'),
]