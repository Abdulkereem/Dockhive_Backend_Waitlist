from django.db import models

class Waitlist(models.Model):
    email = models.EmailField(unique=True)  
    full_name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=40, default="unspecified")
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.email
