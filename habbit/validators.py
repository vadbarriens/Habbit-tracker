from rest_framework.serializers import ValidationError


def validate_habit_or_reward_exclusive(data):
    """Валидатор который исключает одновременный выбор связанной привычки и указания вознаграждения."""
    if data.get('is_pleasant') and data.get('award'):
        raise ValidationError('Нельзя указывать одновременно связанную привычку и вознаграждение')
    return data


def limit_time_completed(value):
    """Валидатор который ограничивает время выполнения до 120 сек."""
    if value > 120:
        raise ValidationError('Время выполнения превышает 120 сек')
    return value


def validate_related_habit_is_pleasant(data):
    """Валидатор где в связанные привычки могут попадать только привычки с признаком приятной привычки."""
    related_habbit = data.get('related_habbit')
    if related_habbit and not related_habbit.is_pleasant:
        raise ValidationError('Связанная привычка должна быть приятной')
    return data


def validate_pleasant_habit_no_rewards_or_related(data):
    """Валидатор где у приятной привычки не может быть вознаграждения или связанной привычки."""
    data_is_pleasant = data.get('is_pleasant', False)
    if data_is_pleasant:
        if data_is_pleasant.get('award'):
            raise ValidationError('У приятной привычки не может быть вознаграждения')
        if data_is_pleasant.get('related_habbit'):
            raise ValidationError('У приятной привычки не может быть связанной привычки')
    return data


def validate_habit_frequency_min_weekly(value):
    """Валидатор который запрещает выполнять привычку реже, чем 1 раз в 7 дней."""
    if value > 7:
        raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
    return value
