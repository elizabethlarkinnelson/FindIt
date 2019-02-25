from django.shortcuts import render, get_object_or_404


from .models import Job, Company


def all_jobs(request):
    all_jobs = Job.objects.all()
    context = {
        'all_jobs': all_jobs,
    }
    return render(request, 'jobs/index.html', context)


def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    company = job.company.name
    context = {
        'job_title': job.title,
        'company_name': company,
        'logo_path': 'jobs/'+ company + '.jpg'
    }
    return render(request, 'jobs/job_detail.html', context)