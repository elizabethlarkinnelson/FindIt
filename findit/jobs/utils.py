
# Company = apps.get_model('jobs', 'Company')
# Job = apps.get_model('jobs', 'Job')
# Requirements = apps.get_model('jobs', 'Requirements')
# Experience = apps.get_model('jobs', 'Experience')
# Compensation = apps.get_model('jobs', 'Compensation')
# Nike = Company(name="Nike", city="New York", state="NY", about="We're awesome")
# Nike.save()

# Nike_Job = Job(title="Senior Director", company=Company.objects.get(name="Nike"), description="Awesome job", link="www.joblink.com")
# Nike_Job.save()

# Nike_Requirement1 = Requirements(job=Job.objects.get(company=Company.objects.get(name="Nike")), description="Know how to code")
# Nike_Requirement1.save()
# Nike_Requirement2 = Requirements(job=Job.objects.get(company=Company.objects.get(name="Nike")), description="SQL")
# Nike_Requirement2.save()

# Nike_Experience1 = Experience(job=Job.objects.get(company=Company.objects.get(name="Nike")), decription="CS Degree")
# Nike_Experience1.save()
# Nike_Experience2 = Experience(job=Job.objects.get(company=Company.objects.get(name="Nike")), decription="10 years experience")
# Nike_Experience2.save()

# Nike_Compensation = Compensation(job=Job.objects.get(company=Company.objects.get(name="Nike")), description="10,000,000")
# Nike_Compensation.save()
