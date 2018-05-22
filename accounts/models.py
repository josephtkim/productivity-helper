from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    experience_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def gain_exp(self, points):
        total_points = self.experience_points + points
        levels_gained = int(total_points / 100)
        self.experience_points = total_points % 100
        self.level += levels_gained
