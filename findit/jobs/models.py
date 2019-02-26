from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, default=None, blank=True)
    state = models.CharField(max_length=2, default=None, blank=True)
    about = models.CharField(max_length=1000, default=None, blank=True)
    embed_link = models.CharField(max_length=300, null=True, default=None, blank=True)


class Job(models.Model):
    title = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True, default=None)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length=300)


class Requirement(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)


class Experience(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)


class Compensation(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

