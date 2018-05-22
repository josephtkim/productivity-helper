from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Goal(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    point_value = models.IntegerField(default=50)

    current_amount_done = models.IntegerField(default=0) # How much current toward goal
    amount_goal = models.IntegerField(default=1) # Total goal
    amount_per_increment = models.IntegerField(default=1)

    units = models.CharField(max_length=50) # Miles, Hours, Minutes, ...
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def increment(self):
        current_total_done = self.current_amount_done + self.amount_per_increment

        if current_total_done >= self.amount_goal:
            self.current_amount_done = self.amount_goal
            self.is_completed = True
            return self.point_value
        else:
            self.current_amount_done = current_total_done
            return 0

    def current_progress(self):
        fraction = float(self.current_amount_done) / self.amount_goal
        fraction *= 100
        return round(fraction, 2)

    def reset_progress(self):
        self.current_amount_done = 0
        self.is_completed = False
