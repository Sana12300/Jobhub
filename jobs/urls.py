
from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs_list, name='jobs_list'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('recruiter/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('recruiter/post-job/', views.post_job, name='post_job'),
     path(
        'recruiter/edit-job/<int:job_id>/',
        views.edit_job,
        name='edit_job'
    ),
    
    path(
    'recruiter/delete-job/<int:job_id>/',
    views.delete_job,
    name='delete_job'
), 
    path('<int:job_id>/', views.job_detail, name='job_detail'),
   
    path('<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('register/', views.register, name='register'),
]
