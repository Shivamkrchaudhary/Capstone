from django.db import models

# Create your models here.
class user_login_info(models.Model):
    Username = models.CharField(max_length=10, unique=True)
    Password  = models.CharField(max_length=30)
    User_Type = models.CharField(max_length=20, default="Manager")

    def __str__(self):
        return self.Username