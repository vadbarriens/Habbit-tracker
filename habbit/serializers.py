from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from habbit.models import Habbit
from habbit.validators import validate_habit_or_reward_exclusive, limit_time_completed, \
    validate_pleasant_habit_no_rewards_or_related, validate_habit_frequency_min_weekly, \
    validate_related_habit_is_pleasant


class HabbitSerializer(ModelSerializer):
    """Сериализатор для привычек"""
    time_completed = serializers.IntegerField(
        validators=[limit_time_completed]
    )
    frequency = serializers.IntegerField(
        validators=[validate_habit_frequency_min_weekly]
    )

    class Meta:
        """Метаданные"""
        model = Habbit
        fields = '__all__'
        read_only_fields = ['owner']
        validators = [validate_habit_or_reward_exclusive, validate_pleasant_habit_no_rewards_or_related,
                      validate_related_habit_is_pleasant]
