from django.db import models

# Create your models here.



JOB_TUPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)
class Job(models.Model):
    title = models.CharField(max_length=200)

    job_type = models.CharField(max_length=20, choices=JOB_TUPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateField(auto_now=True)
    # time data in database
    Vancncy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)


    def __str__(self):
        return self.title

