from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from tools.models import Tool
from django.utils import timezone

# Create your models here.

class Idea(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="image/")
    content = models.CharField(max_length=255)
    interest = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null =True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'idea')