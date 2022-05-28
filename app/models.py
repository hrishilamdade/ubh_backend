import email
from telnetlib import STATUS
from djongo import models

# Create your models here.

STATUS_CHOICES = (
    (1, 'contacted'),
    (2,'inprocess'),
    (3,'verified'),
    (4,'refused'),
)

class Empanelment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    reference_id = models.CharField(max_length=500)
    status = models.IntegerField(default=2,choices=STATUS_CHOICES)

    