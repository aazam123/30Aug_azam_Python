from django.db import models

# Create your models here.

class studinfo(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)
    repeatepassword=models.CharField(max_length=20)
    address=models.TextField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    address=models.TextField()

    def __str__(self) -> str:
        return self.name
