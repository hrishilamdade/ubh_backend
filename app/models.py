from djongo import models

# Create your models here.

STATUS_CHOICES = (
    ('contacted','contacted'),
    ('inprocess','inprocess'),
    ('verified','verified'),
    ('refused','refused'),
)

class Empanelment(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50,default="")
    last_name = models.CharField(max_length=50,default="")
    email = models.EmailField(max_length=50,unique=True,null=True,blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    reference_id = models.CharField(max_length=500)
    project_topic = models.CharField(max_length=200,default="Project Topic")
    comments = models.JSONField(default=[],null=True, blank=True)
    status = models.CharField(max_length=20, default="contacted",choices=STATUS_CHOICES)

    
class MetaExpert(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50,default="")
    last_name = models.CharField(max_length=50,default="")    
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    reference_id = models.CharField(max_length=500)
    project_topic = models.CharField(max_length=200,default="Project Topic")
    biography = models.TextField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    geography = models.CharField(max_length=200,null=True,blank=True)
    skills = models.JSONField(default=[] ,null=True, blank=True)
    profile_complete = models.BooleanField(default=False)

