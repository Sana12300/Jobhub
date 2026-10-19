
from django import forms
from .models import Job,JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'applicant_name',
            'applicant_email',
            'resume',
            'cover_letter'
        ]

        widgets = {
            'applicant_name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name'
            }),
            'applicant_email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address'
            }),
            'cover_letter': forms.Textarea(attrs={
                'placeholder': 'Why are you applying for this job?',
                'rows': 5
            }),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title',
            'company',
            'location',
            'salary',
            'job_type',
            'experience',
            'description',
            'responsibilities',
            'requirements',
            'skills',
        ]