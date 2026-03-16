from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Класс - пользователи"""
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Введите почту')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='Город',
                            help_text='Введите название города')
    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name='Телефон',
                             help_text='Введите номер телефона')
    avatar = models.ImageField(upload_to='users/avatar', blank=True, null=True, verbose_name='Аватар',
                               help_text='Загрузите ваш аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        """Метаданные"""
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        """Строковое представление"""
        return self.email
