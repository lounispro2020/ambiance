from django.db import models

# Create your models here.

class Temperature(models.Model):

    VALEUR_TEMP = models.CharField(max_length=10)
    #moment = models.CharField(max_length=60)


    def __str__(self):
        return self.VALEUR_TEMP


        