from django.db import models
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(max_length=50, verbose_name='Почта')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    theme = models.CharField(max_length=50, verbose_name='Тема обращений')
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'landing'
        ordering = ["-date_created", "-first_name", ]
        verbose_name = "Обращения"
        verbose_name_plural = "Обращении"

    def __str__(self):
        return f"От {self.first_name} по этому дату {self.date_created}"