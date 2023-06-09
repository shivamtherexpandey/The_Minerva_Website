from django.db import models


# Create your models here.

class Submit_Data(models.Model):
    Email = models.EmailField()
    Message = models.TextField()

    def __str__(self):
        return self.Email
