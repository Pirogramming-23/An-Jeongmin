from django import forms
from .models import Review

class ReviewForm(forms.ModelForm): # 자동으로 폼 만들기
    class Meta:
        model = Review
        fields = '__all__'