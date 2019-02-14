from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=50)
    company = models.IntegerField()

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    company_logo = models.ImageField()
