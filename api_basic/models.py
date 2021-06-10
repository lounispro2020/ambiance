from django.db import models

# Create your models here.

class Temperature(models.Model):

    temperature = models.CharField(max_length=10)
    #moment = models.CharField(max_length=60)

    moment= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.temperature

    class Meta:
        db_table = "temperature"

        