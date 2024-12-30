from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobForm
from .models import Job

def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            company = request.user.company
            form.save(company=company)
            return redirect('list-jobs')
    else:
        form = JobForm()
    return render(request, 'job/create_job.html', {'form': form})

def list_job(request):
    company = request.user.company
    jobs = Job.objects.filter(company=company)
    return render(request, 'job/list_job.html', {'jobs': jobs})

def update_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if job.company != request.user.company:
        return redirect('list-jobs')
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('list-jobs')
    else:
        form = JobForm(instance=job)

    return render(request, 'job/update_job.html', {'form': form, 'job':job})
        
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if job.company != request.user.company:
        return redirect('list-jobs')  
    
    if request.method == 'POST':
        job.delete()
        return redirect('list-jobs')  
    
    return render(request, 'job/confirm_delete_job.html', {'job': job})