from django.db import models

class Job(models.Model):
    company = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    date_start = models.DateField()
    date_end = models.DateField()
