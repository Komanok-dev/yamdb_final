
![# Проект YaMDb](https://github.com/Komanok-dev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)



Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «изобразительное искусство» или «Ювелирка»).
​
## Стек технологий: 
* Python3
* Django REST Framework
* Postgres
* Docker
* Git
---

Документация и возможности API:
К проекту подключен redoc. Для просмотра документации используйте эндпойнт redoc/

## Как запустить проект: 
​
**Клонировать репозиторий и создайте .env файл в директории infra/, в котором должны содержаться следующие переменные:**
```
DEBUG=False
SECRET_KEY=sefmioesjf89234uj3q2irnwjuifhwurwfknmsjefneushes
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

**Из папки infra/ соберите образ при помощи docker-compose:**
```
docker-compose up -d --build
```
​
**Примените миграции:**
```
docker-compose exec web python manage.py migrate
```

**Для доступа к админке создайте суперюзера:**
```
docker-compose exec web python manage.py createsuperuser 
```
​​
**Соберите статику:**
​```
docker-compose exec web python manage.py collectstatic --no-input 
```

Host: http://komanok.hopto.org