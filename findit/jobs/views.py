from django.shortcuts import render
from django.http import HttpResponse

from .models import Job


def index(request):
    all_jobs = Job.objects.all()
    return HttpResponse(all_jobs)
