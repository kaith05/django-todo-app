from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="タイトル")
    description = models.TextField(blank=True, null=True, verbose_name="詳細")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

    def __str__(self):
        return self.title