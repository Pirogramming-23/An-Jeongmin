from django.db import models

# Create your models here.
class Review(models.Model):
    GENRE_CHOICES = [
        ('DR', '드라마'),
        ('CM', '코미디'),
        ('AC', '액션'),
        ('RM', '로맨스'),
        ('TH', '스릴러'),
        ('HR', '공포'),
        ('SF', 'SF'),
        ('AN', '애니메이션'),
        ('DC', '다큐멘터리'),
        ('ET', '기타'),
    ]
    title = models.CharField(max_length=50)
    poster = models.ImageField(upload_to="poster/")
    release_year = models.PositiveIntegerField()
    director = models.CharField(max_length=50)
    cast = models.CharField(max_length=100)
    genre = models.CharField(max_length=2, choices= GENRE_CHOICES)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    running_time = models.PositiveIntegerField(help_text="단위: 분")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): # 인스턴스 출력시 가독성 높이기
        return f"{self.title} ({self.release_year})"