from django.db import models

# Create your models here.
class contact(models.Model):
    Name=models.CharField(max_length=20)
    Email_Id=models.CharField(max_length=50)
    Mobile_no=models.IntegerField()
    Message=models.CharField(max_length=500)
