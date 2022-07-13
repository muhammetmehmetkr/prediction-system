from django.db import models

# Create your models here.

class Prediction_Results(models.Model):

    age = models.FloatField()
    sex = models.FloatField()
    bmi = models.FloatField()
    children = models.FloatField()
    smooker = models.FloatField()
    regression = models.CharField(max_length=30)

    def __str__(self):
        return self.regression
