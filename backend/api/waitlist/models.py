from django.db import models

class Waitlist(models.Model):
    email = models.EmailField(unique=True)  
    full_name = models.CharField(max_length=50)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.email
