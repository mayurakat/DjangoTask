from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here
    

   




class blogs(models.Model):
    topic = models.CharField(max_length=50)
    description = models.TextField()
  
    author = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.topic

