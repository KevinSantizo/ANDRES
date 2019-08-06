from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50, help_text='Enter his First Name')
    last_name = models.CharField(max_length=50, help_text='Enter his Last Name')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
