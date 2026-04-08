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
cd django_rest
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
Создайте файл .env и заполните его:
```
cp .env.example .env
```
Соберите и запустите контейнеры:
```
docker-compose up --build -d
```
После запуска проект будет доступен по адресу:
```
http://localhost:8000
```
Остановка проекта:
```
docker-compose down
```
Остановка с удалением volumes:
```
docker-compose down -v
```
Пересборка проекта:
```
docker-compose up --build -d
```
Просмотр логов:
```
docker-compose logs <service_name>  # web, db, redis, celery, celery-beat
```

## Структура проекта
- /code - корневая директория проекта внутри контейнера

- /code/static - статические файлы

- /var/lib/postgresql/data - данные PostgreSQL

- /data - данные Redis

- /var/lib/celery - состояние Celery Beat
