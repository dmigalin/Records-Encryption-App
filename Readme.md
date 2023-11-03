## PET проект API "Зашифрованный текст"
Анонимная API для размещения зашифрованных сообщений,
которые невозможно прочитать через час после размещения.

### Стек технологий
`Nginx`
`FastAPI`
`Uvicorn`
`SQLAlchemy`
`Postgresql`
`Pymongo` + `Motor`
`Mongodb`
`cryptography`
`Docker`

## Для пользователей Windows
### Запуск приложения
1. Создать виртуальное окружение и установить зависимости
2. Запустить приложение `docker compose -f docker-compose.yaml up -d`
3. Сгенерировать новые миграции
`docker exec app sh -c "alembic revision --autogenerate -m 'database_init'"`
4. Обновляем новые миграции в базе данных Postgresql
`docker exec app sh -c "alembic upgrade head"`

### Полезные комманды для вызова из терминала
1. `make migrate`
    - генерируем новые миграции для базы данных Postgresql
2. `docker exec app sh -c "alembic upgrade head"`
    - обновляем новые миграции в базе данных Postgresql 
3. `docker exec app sh -c "rm -R passwords && mkdir passwords"`
    - очищает папку `passwords`
4. `docker exec app sh -c "pytest -s -v tests/*"`
    - при запущенном приложении звупускает тесты pytest

## Для пользователей Mac и Linux
### Запуск приложения
1. Создать виртуальное окружение и установить зависимости
2. Запуск приложения впервые - `make start`
3. Запустить приложение только с обновлением миграций - `make up`

### Остановка приложения
1. `make stop` - останавливает работу контейнеров
2. `make down` - останавливает работу контейнеров и удаляет их

### Полезные комманды для вызова из терминала
1. `make migrate`
    - генерируем новые миграции и вносим их в базу данных Postgresql
2. `make clean pw`
    - очищает папку `passwords`
3. `make test`
    - при запущенном приложении звупускает тесты pytest


### Настройка виртуального окружения
1. В корневой папке необходимо создать файл .env и указать следующие переменные:
    - MONGO_USER =''
    - MONGO_PASSWORD =''
    - POSTGRES_USER=''
    - POSTGRES_PASSWORD =''
    - UVI_HOST='0.0.0.0'              # Example
    - UVI_PORT=8000                   # Example
    - SCHEDULER_HOST='0.0.0.0'        # Example
    - SCHEDULER_PORT=8010             # Example
