
from django.shortcuts import render, get_object_or_404,redirect
from .models import Job, JobApplication
from .forms import JobApplicationForm,JobForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required,user_passes_test

def staff_required(view_func):
    return user_passes_test(
        lambda user: user.is_staff
    )(view_func)
    
def jobs_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs/jobs.html', {'jobs': jobs})


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            
            if JobApplication.objects.filter(
                job=job,
                applicant_email=application.applicant_email
            ).exists():
                form.add_error(
                    'applicant_email',
                    'You have already applied for this job.'
                )
            else:
                application.save()
                return render(
                    request,
                    'jobs/application_success.html',
                    {'job': job}
                )
    else:
        form = JobApplicationForm()

    return render(
        request,
        'jobs/apply.html',
        {
            'form': form,
            'job': job
        }
    )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('jobs_list')
    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )
    
@login_required
def my_applications(request):
        applications = JobApplication.objects.filter(
            user=request.user
        ).select_related('job').order_by('-applied_at')

        return render(
            request,
            'jobs/my_applications.html',
            {'applications': applications}
        )
        
@staff_required
def recruiter_dashboard(request):
    jobs = Job.objects.all().order_by('-created_at')

    return render(
        request,
        'jobs/recruiter_dashboard.html',
        {'jobs': jobs}
    )
    
    
@staff_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('recruiter_dashboard')
    else:
        form = JobForm()

    return render(
        request,
        'jobs/post_job.html',
        {'form': form}
    )
    
@staff_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            form.save()
            return redirect('recruiter_dashboard')
    else:
        form = JobForm(instance=job)

    return render(
        request,
        'jobs/edit_job.html',
        {'form': form, 'job': job}
    )
    
@staff_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        job.delete()
        return redirect('recruiter_dashboard')

    return render(
        request,
        'jobs/delete_job.html',
        {'job': job}
    )