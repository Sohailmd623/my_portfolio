from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    date =  models.DateTimeField()
    Tools_Used= models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:80]

    def pub_date(self):
        return self.date.strftime('%b %e %Y')