from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=250)
    des=models.TextField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name


class team(models.Model):
    photo=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    detail=models.TextField()

    def __str__(self):
        return self.name
