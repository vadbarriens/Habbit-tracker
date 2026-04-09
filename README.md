# Трекер привычек
## 📌 Описание проекта
Сервис позволяет пользователям создавать привычки разных направлений (приятные и полезные), связывать их между собой и отправлять напоминание о их выполнении. 


## 🚀 Функциональность
## Основная часть (обязательная по ТЗ):
#### ✅ CRUD для клиентов 
#### ✅ CRUD для привычек
### Дополнительная часть (расширение функциональности):
#### ✅ Регистрация и аутентификация пользователей (через email)
#### ✅ Ограничение доступа: пользователь видит только свои данные
#### ✅ Роли:неавторизованные пользователи и владельцы привычек
#### ✅ CRUD операции описаны через ViewSet и Generic классы
#### ✅ Описаны сериализаторы для каждой модели
#### ✅ Описана пагинация 
#### ✅ Созданы валидаторы 
#### ✅ Описан пермишн для владельцев и обычных пользователей
#### ✅ Написаны тесты через unittest
## 🛠️ Технологии
#### Django REST
#### PostgreSQL
#### unittest
#### DRF
#### JWT auth system
#### Swagger
#### CORS
#### Postman

## 📂 Установка
Клонировать репозиторий:
```
 git clone https://github.com/yourname/Habbit_tracker.git`
cd Habbit_tracker
```

Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
Установить зависимости:
```
pip install -r requirements.txt
```

Применить миграции:
```
python manage.py migrate
```
Создать суперпользователя:
```
python manage.py createsuperuser
```

## CI/CD
### Установка Docker и Docker Compose
Обновление пакетов:
```
sudo apt update
```
установка Docker:
```
sudo apt install docker-compose
```
###  Настройка SSH-доступа
Сгенерируйте SSH-ключ на локальной машине:
```
ssh-keygen -t ed25519 -f ~/.ssh/deploy_key -N ""
```
Скопируйте публичный ключ на сервер:
```
ssh-copy-id -i ~/.ssh/deploy_key.pub ваш_пользователь@ip_сервера
```
Проверьте подключение:
```
ssh -i ~/.ssh/deploy_key ваш_пользователь@ip_сервера
```

## Подготовка GitHub Secrets
В настройках репозитория GitHub:

Перейдите в Settings → Secrets and variables → Actions

Создайте новые секреты:

DOCKER_HUB_USERNAME - ваш логин на Docker Hub

DOCKER_HUB_ACCESS_TOKEN - токен доступа Docker Hub

SSH_PRIVATE_KEY - содержимое файла deploy_key (приватный ключ)

SSH_USER - пользователь сервера (например, ubuntu)

SERVER_IP - IP-адрес вашего сервера
 ## Workflow CI/CD
При каждом пуше в ветку develop автоматически выполняются:

1. Линтинг кода (Flake8)

2. Запуск тестов (pytest)

3. Сборка Docker-образа и публикация в Docker Hub

4. Деплой на удалённый сервер


### Адрес сервера
```
ssh -l final_task 158.160.252.144
```