from django.db import models
from django.contrib.auth.models import User  # Django의 기본 사용자 모델

# Create your models here.
class TODO(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length = 255)
    created_date = models.DateTimeField(auto_now_add=True)