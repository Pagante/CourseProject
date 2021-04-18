from django.db import models

# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='Photos/')

    def __str__(self):
        return self.course_title
