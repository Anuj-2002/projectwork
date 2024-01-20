from django.db import models

# Create your models here.


class Mail(models.Model):
    full_names = models.TextField(verbose_name="Full Names ")
    message = models.TextField(verbose_name="Description ")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_names
