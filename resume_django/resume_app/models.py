from django.db import models

# Create your models here.
class Resume(models.Model):
     name=models.CharField(max_length=199)
     email=models.EmailField()
     phone=models.CharField(max_length=90)
     education=models.TextField()
     skills=models.TextField()
     experience=models.TextField()


