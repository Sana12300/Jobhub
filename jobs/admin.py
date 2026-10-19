from django.contrib import admin
from .models import Job, JobApplication


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company',
        'location',
        'job_type',
        'experience',
        'salary',
        'created_at'
    )

    search_fields = (
        'title',
        'company',
        'location'
    )

    list_filter = (
        'job_type',
        'experience'
    )
    
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'applicant_name',
        'applicant_email',
        'job',
        'applied_at'
    )

    list_filter = ('applied_at', 'job')

    search_fields = (
        'applicant_name',
        'applicant_email'
    )
