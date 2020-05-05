from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    date =  models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title


    def pub_date(self):
            return self.date.strftime('%b %e %Y')
