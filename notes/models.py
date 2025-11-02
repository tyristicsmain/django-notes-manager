from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    category = models.IntegerField(default=3)
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return self.title


