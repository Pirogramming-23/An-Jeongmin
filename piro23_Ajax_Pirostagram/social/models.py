from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=20)
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)