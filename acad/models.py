from django.db import models

# Create your models here.

class Acad(models.Model):
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    score = models.FloatField(max_length=10)

    def __str__(self):
        return self.title


    def pub_date(self):
            return self.date.strftime('%b %e %Y')