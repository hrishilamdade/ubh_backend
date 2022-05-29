import email
from telnetlib import STATUS
from djongo import models

# Create your models here.

STATUS_CHOICES = (
    ('contacted','contacted'),
    ('inprocess','inprocess'),
    ('verified','verified'),
    ('refused','refused'),
)

class Empanelment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    reference_id = models.CharField(max_length=500)
    status = models.CharField(max_length=20, default="contacted",choices=STATUS_CHOICES)

    