from django.db import models

# Create your models here.
class MostTraded(models.Model):
    index = models.IntegerField(primary_key=True)
    symbol = models.TextField()
    volume = models.FloatField()

    class Meta:
        #managed = False
        db_table = 'most_traded'