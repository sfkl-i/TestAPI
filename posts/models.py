from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    link = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    amount_of_upvotes = models.PositiveIntegerField(default=0, verbose_name="Оценок")

    class Meta:
        ordering = ["-amount_of_upvotes"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name="Статья",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=2500)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return str(self.created)
