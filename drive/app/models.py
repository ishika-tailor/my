from django.db import models


# Create your models here.

class Empinsert(models.Model):
    name = models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    number = models.CharField(max_length=200)
    age = models.CharField(max_length=5)
    state = models.CharField(max_length=50)
    msg = models.TextField(max_length=200)

    class Meta:
        db_table: "dri"
