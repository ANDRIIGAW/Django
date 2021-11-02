from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.titel

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'