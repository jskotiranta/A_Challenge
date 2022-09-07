from django.db import models

# Create your models here.
class MostTraded(models.Model):
    index = models.IntegerField(primary_key=True)
    symbol = models.TextField(max_length=6)
    volume = models.FloatField()
    def __str__(self):
        return MostTraded({self.symbol},{self.volume})

    class Meta:
        managed = True
        db_table = 'most_traded'