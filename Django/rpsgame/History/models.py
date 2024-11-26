from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class history(models.Model):
    user=models.OneToOneField(User , on_delete=models.CASCADE)
    winrate=models.FloatField(max_length=3, default=0)
    historyarr=models.CharField(max_length=100 , default="")
    def __str__(self) :
        return self.historyarr