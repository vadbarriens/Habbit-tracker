from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from habbit.models import Habbit
from habbit.paginators import HabbitPagination
from habbit.permissions import IsOwner, IsPublicOrOwner
from habbit.serializers import HabbitSerializer


class HabitCreateApiView(CreateAPIView):
    """Контроллер для создания привычки"""
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer

    def perform_create(self, serializer):
        """Привязка пользователя при создании"""
        serializer.save(owner=self.request.user)


class HabitListApiView(ListAPIView):
    """Контроллер для просмотра списка привычек"""
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    pagination_class = HabbitPagination

    def get_queryset(self):
        """Отображение списка привычек только для создателя"""
        return Habbit.objects.filter(owner=self.request.user)


class HabitPublicListApiView(ListAPIView):
    """Контроллер для просмотра списка публичных привычек"""
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    pagination_class = HabbitPagination

    def get_queryset(self):
        """Отображение списка только публичных привычек"""
        return Habbit.objects.filter(is_public=True)


class HabitUpdateApiView(UpdateAPIView):
    """Контроллер для обновления привычки"""
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsOwner]


class HabitRetrieveApiView(RetrieveAPIView):
    """Контроллер для изменения привычки"""
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsPublicOrOwner]


class HabitDestroyApiView(DestroyAPIView):
    """Контроллер для удаления привычки"""
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerializer
    permission_classes = [IsOwner]
