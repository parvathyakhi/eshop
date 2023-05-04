from django.db import models

# Create your models here.
class system(models.Model):
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
