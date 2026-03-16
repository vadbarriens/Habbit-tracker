from django.db import models
from django.db.models import SET_NULL

from users.models import User


class Habbit(models.Model):
    """Модель - привычка"""
    FREQUENCY_CHOICES = {
        1: 'Ежедневно',
        2: 'Каждые 2 дня',
        3: 'Каждые 3 дня',
        4: 'Каждые 4 дня',
        5: 'Каждые 5 дней',
        6: 'Каждые 6 дней',
        7: 'Еженедельно',

    }
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь',
                              help_text='Укажите пользователя')
    place = models.CharField(max_length=100, verbose_name='Место', help_text='Выберите место')
    time = models.TimeField(verbose_name='Время', help_text='Укажите время')
    action = models.CharField(max_length=350, verbose_name='Действие', help_text='Опишите действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habbit = models.ForeignKey('self', on_delete=SET_NULL, null=True, blank=True,
                                       verbose_name='Приятная привычка', help_text='Выберите приятную привычку')
    frequency = models.PositiveSmallIntegerField(choices=FREQUENCY_CHOICES, default=1, verbose_name='Периодичность',
                                                 help_text='Выберите периодичность')
    award = models.CharField(max_length=255, blank=True, null=True, verbose_name='Вознаграждение',
                             help_text='Опишите вознаграждение')
    time_completed = models.PositiveSmallIntegerField()
    is_public = models.BooleanField(default=False, verbose_name='Публикация')

    class Meta:
        """Метаданные"""
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        """Строковое представление"""
        return self.action
