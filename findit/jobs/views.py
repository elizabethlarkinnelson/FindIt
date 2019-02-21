from django.shortcuts import render
from django.http import HttpResponse

from .models import Job


def all_jobs(request):
    all_jobs = Job.objects.all()
    return HttpResponse(all_jobs)

def job_detail(request, job_id):
    return HttpResponse("You're looking at job %s" % job_id)