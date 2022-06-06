from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.forms import BooleanField

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Статья")
    content = models.TextField(blank=True, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at', '-title']
