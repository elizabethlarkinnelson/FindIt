from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)

class Job(models.Model):
    title = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    link = models.CharField(max_length=50)



    
