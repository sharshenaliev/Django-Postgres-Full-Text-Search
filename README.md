# Развертывание проекта


## Настройка окружения

Создайте `.env` файл заполните:

```shell
POSTGRES_DB=test
POSTGRES_USER=test
POSTGRES_PASSWORD=test
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
SECRET_KEY=
ALLOWED_HOSTS=
CSRF_TRUSTED_ORIGINS=
```

## Сборка Docker образа

1. Запустите Docker Compose build:

    ```
    make build
    ```
   
2. Запустите миграции:

    ```
    make migrate
    ```
   
3. Запустите тесты:

    ```
    make test
    ```

4. При желании загрузить dump:

    ```
    make loaddata
    ```

## Работа с API

1. Swagger UI `http://localhost:8000/docs`.

2. ReDoc `http://localhost:8000/redoc`.

3. Admin panel `http://localhost:8000/admin`. 

4. Кэширование для `list`
`http://localhost:8000/api/v1/products/`. 