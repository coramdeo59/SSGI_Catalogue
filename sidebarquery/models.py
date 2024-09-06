from django.db import models

# Create your models here.
class ssgi(models.Model):
  date=models.DateTimeField(null=True)
  folder=models.CharField(default=None)


