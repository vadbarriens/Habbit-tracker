from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateApiView(CreateAPIView):
    """Контроллер для создания пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListApiView(ListAPIView):
    """Контроллер для просмотра списка пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(UpdateAPIView):
    """Контроллер для обновления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserRetrieveApiView(RetrieveAPIView):
    """Контроллер для редактирования пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserDestroyApiView(DestroyAPIView):
    """Контроллер для удаления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
