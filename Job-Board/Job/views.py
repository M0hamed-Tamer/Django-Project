from django.shortcuts import render
from .models import Job
# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    print(job_list)
    context = {}
    # object all jobs
    return render(request, 'job/jobs.html',context)
    
def job_detail(request):
    job_id = request.GET.get('job_id')
    job = Job.objects.get(id=job_id)
    context = {}
    context['job'] = job
    return render(request, 'job/job_detail.html', context)
    