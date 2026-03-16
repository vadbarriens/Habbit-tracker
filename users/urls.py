from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

from users.views import UserCreateApiView, UserDestroyApiView, UserUpdateApiView, UserRetrieveApiView, UserListApiView

app_name = UsersConfig.name

urlpatterns = [
    path('list/', UserListApiView.as_view(), name='user_list'),
    path('<int:pk>/detail/', UserRetrieveApiView.as_view(), name='user_retrieve'),
    path('register/', UserCreateApiView.as_view(), name='user_create'),
    path('<int:pk>/update/', UserUpdateApiView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDestroyApiView.as_view(), name='user_delete'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

]
