from django.db import models

# Create your models here.
class PortFolio(models.Model):
    category = models.CharField(max_length=100)
    project_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Photos/')

    def __str__(self):
        return self.category
