from django.db import models

class usertab(models.Model):
    fname=models.CharField(name="fname" ,max_length=50)
    lname=models.CharField(name="lname",max_length=50)
    email=models.EmailField()
    username=models.CharField(name="username",max_length=15)
    passw=models.CharField(name="passw",max_length=15)
    con_passw=models.CharField(name="cpassw",max_length=15)

