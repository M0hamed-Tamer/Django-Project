from django.shortcuts import render
from .models import Job
# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    

    
    context = {'jobs': job_list}

    return render(request, 'job/views_modils.html',context)    
def job_detail(request, id):
    # احصل على الوظيفة باستخدام المعامل الذي تم تمريره عبر الـ URL
    job = Job.objects.get(id=id)
    
    # جهز القالب مع البيانات المناسبة
    context = {
        'job': job
    }
    
    return render(request, 'job/job_detail.html', context)