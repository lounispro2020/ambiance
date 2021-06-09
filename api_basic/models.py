from django.db import models

# Create your models here.

class Temperature(models.Model):

    VALEUR_TEMP = models.CharField(max_length=10)
    #moment = models.CharField(max_length=60)

    Timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.VALEUR_TEMP

class Playlist(models.Model):
    name = models.CharField(max_length=20)

class Music(models.Model):
    name = models.CharField(max_length=20)
    path = models.CharField(max_length=40)
    Format = models.CharField(max_length=5)
    artist = models.CharField(max_length=10)
    playlist = models.ForeignKey('Playlist',on_delete=models.CASCADE)

class Led_color(models.Model):
    color = models.CharField(max_length = 11)

class Algorithmes(models.Model):
    begin_time = models.TimeField()
    end_time = models.TimeField()
    begin_month = models.DateField()
    end_month = models.DateField()
    max_temp = models.DecimalField(max_digits = 2, decimal_places = 0)
    min_temp = models.DecimalField(max_digits = 2, decimal_places = 0)
    led = models.ForeignKey('Led_color',on_delete=models.CASCADE)
    playlist = models.ForeignKey('Playlist',on_delete=models.CASCADE)

        