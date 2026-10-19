from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):

    JOB_TYPES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
    ]

    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)

    job_type = models.CharField(
        max_length=30,
        choices=JOB_TYPES
    )

    experience = models.CharField(max_length=50)

    description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()

    skills = models.CharField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class JobApplication(models.Model):
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"

    
    class Meta:
         unique_together = ('job', 'applicant_email')
