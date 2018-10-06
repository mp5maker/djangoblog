from django.db import models

# Create your models here.
class App(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "List of Landing Pages"