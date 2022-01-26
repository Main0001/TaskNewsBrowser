from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    anons = models.CharField(max_length=255, verbose_name='Анонс')
    full_text = models.TextField(verbose_name='Полный текст')
    date = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

