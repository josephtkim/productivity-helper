from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    point_value = models.IntegerField(default=10)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def title_summary(self):
        # return self.title[:100]
        return self.title
