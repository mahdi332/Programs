from django.db import models

# Create your models here.
class GameARR(models.Model):
    choice_text=models.CharField(max_length=10)
    def __str__(self):
        return self.choice_text