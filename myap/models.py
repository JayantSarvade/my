from django.db import models

# Create your models here.
class Mydb(models.Model):
    age= models.IntegerField(max_length=3)


    def __str__(self):
        return str(self.age)