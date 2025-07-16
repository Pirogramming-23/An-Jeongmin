from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=50, unique=True)
    kind = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name