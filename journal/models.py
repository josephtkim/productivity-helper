from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.title

    def show_summary(self):
        if len(self.content) > 400:
            return self.content[:400] + "..."
        else:
            return self.content

    def clean_date(self):
        return self.published_date.strftime("%B %d %Y")
