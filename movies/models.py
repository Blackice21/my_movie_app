from django.db import models
from django.core.validators import MaxValueValidator


class Movies(models.Model):
    picture = models.URLField(max_length=900, default='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSSSDAflI2W07ixtGLC1dxDGHkR5x9rek2BHlY3q07ZoxaTwv_d&usqp=CAU')
    name = models.CharField(max_length=200)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    notes = models.TextField(max_length=2000, default='')

    def __str__(self):
        return self.name
