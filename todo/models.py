from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=155, null=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)


