from django.db import models

class Person(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Company_name=models.CharField(max_length=20)
    Email_name=models.CharField(max_length=20)
    Subject_name=models.CharField(max_length=20)
    Password_name=models.CharField(max_length=500,blank=True,null=True)
    Adress_name=models.TextField(max_length=20)
    is_active=models.BooleanField(default=True)
