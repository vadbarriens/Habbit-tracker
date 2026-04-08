from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habbit.models import Habbit
from users.models import User


class HabitCRUDTestCase(APITestCase):
    def setUp(self):
        User.objects.all().delete()
        # Создаем пользователей
        self.user = User.objects.create(
            username='testuser',
            email='test@test.com',
            password='testpass'
        )

        # URL для тестирования
        self.list_url = reverse('users:user_list')
        self.create_url = reverse('users:user_create')
        self.retrieve_url = reverse('users:user_retrieve', kwargs={'pk': self.user.pk})
        self.update_url = reverse('users:user_update', kwargs={'pk': self.user.pk})
        self.delete_url = reverse('users:user_delete', kwargs={'pk': self.user.pk})
        self.refresh_url = reverse('users:token_refresh')
        self.login_url = reverse('users:login')

    def test_user_create(self):
        """Тест создания пользователя"""
        self.client.force_authenticate(user=self.user)
        data = {
            'email': 'newemail@test.com',
            'city': 'new city',
            'phone': 'new phone',
            'tg_chat_id': '99999',
            'password': 'new password'
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_retrieve(self):
        """Тест получения пользователя"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_user_update(self):
        """Тест обновления пользователя"""
        self.client.force_authenticate(user=self.user)
        data = {'city': 'Updated city'}
        response = self.client.patch(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.city, 'Updated city')

    def test_user_delete(self):
        """Тест удаления пользователя"""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habbit.objects.count(), 0)
