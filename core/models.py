from django.db import models

# Create your models here.
class Directory(models.Model):
    s_link = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return self.title