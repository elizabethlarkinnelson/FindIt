from django.shortcuts import render, get_object_or_404


from .models import Job, Company, Requirement, Experience, Compensation


def all_jobs(request):
    all_jobs = Job.objects.all()
    context = {
        'all_jobs': all_jobs,
    }
    return render(request, 'jobs/index.html', context)


def job_detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    company = job.company
    requirements = Requirement.objects.filter(job=job)
    experiences = Experience.objects.filter(job=job)
    compensation = Compensation.objects.filter(job=job)

    context = {
        'job': job,
        'company': company,
        'requirements': requirements,
        'experiences': experiences,
        'compensation': compensation,
        'logo_path': 'jobs/'+ company.name + '.jpg'
    }
    return render(request, 'jobs/job_detail.html', context)