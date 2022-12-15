from django.db import models

# Create your models here.
class SignIn(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)
    ipaddress = models.CharField(max_length=1000, default='1')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    def __str__(self):
        return self.email