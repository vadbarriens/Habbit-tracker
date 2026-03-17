from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habbit.models import Habbit
from users.models import User


class HabitCRUDTestCase(APITestCase):
    def setUp(self):
        # Создаем пользователей
        self.user_test = User.objects.create(
            email='test@test.com',
            password='testpass'
        )
        # Создаем полезную привычку
        self.habit = Habbit.objects.create(
            owner=self.user_test,
            place='test place',
            time='12:00:00',
            action='test action',
            is_pleasant=False,
            award='test award',
            frequency=1,
            time_completed=60,
            is_public=False

        )

        # Создаем приятную привычку
        self.pleasant_habit = Habbit.objects.create(
            owner=self.user_test,
            place='test place 2',
            time='13:00:00',
            action='test action 2',
            is_pleasant=True,
            frequency=1,
            time_completed=100,
            is_public=False

        )

        # Создаем публичную привычку
        self.pleasant_habit = Habbit.objects.create(
            owner=self.user_test,
            place='test place 3',
            time='13:00:00',
            action='test action 3',
            is_pleasant=True,
            frequency=1,
            time_completed=100,
            is_public=True

        )

        # URL для тестирования
        self.list_url = reverse('habbit:habit_list')
        self.create_url = reverse('habbit:habit_create')
        self.retrieve_url = reverse('habbit:habit_retrieve', kwargs={'pk': self.habit.pk})
        self.update_url = reverse('habbit:habit_update', kwargs={'pk': self.habit.pk})
        self.delete_url = reverse('habbit:habit_delete', kwargs={'pk': self.habit.pk})
        self.public_url = reverse('habbit:public_list')

    def test_habit_create_user(self):
        """Тест создания привычки"""
        self.client.force_authenticate(user=self.user_test)
        data = {
            'place': 'new place',
            'time': '13:00:00',
            'action': 'new action',
            'is_pleasant': False,
            'frequency': 1,
            'award': 'new award',
            'time_completed': 60,
            'is_public': False
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_retrieve_user(self):
        """Тест получения привычки"""
        self.client.force_authenticate(user=self.user_test)
        response = self.client.get(self.retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['action'], self.habit.action)

    def test_habit_update_user(self):
        """Тест обновления привычки"""
        self.client.force_authenticate(user=self.user_test)
        data = {'action': 'Updated action'}
        response = self.client.patch(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.action, 'Updated action')

    def test_habit_delete_user(self):
        """Тест удаления привычки"""
        self.client.force_authenticate(user=self.user_test)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habbit.objects.count(), 2)

    def test_habit_list_authenticated(self):
        """Тест получения списка привычек авторизованным пользователем"""
        self.client.force_authenticate(user=self.user_test)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_list_unauthenticated(self):
        """Тест получения списка привычек неавторизованным пользователем"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_habit_public_list(self):
        """Тест получения опубликованного списка """
        self.client.force_authenticate(user=self.user_test)
        response = self.client.get(self.public_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
