from django.db import models

class UserDetails(models.Model):
    email = models.EmailField(max_length=100, primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=12, blank=True)
    
    def __str__(self):
        return self.username
