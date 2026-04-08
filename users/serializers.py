from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор для пользователя"""

    class Meta:
        """Метаданные"""
        model = User
        fields = ['id', 'email', 'phone', 'city', 'password']
        read_only_fields = ['id']
