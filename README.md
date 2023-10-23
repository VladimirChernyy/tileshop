# Онлайн магазин 
## Описание
Магазин продажи инструмента и расходных материалов для обработки керамогранита

![2023-10-23_13-48](https://github.com/VladimirChernyy/tileshop/assets/116533449/0e35f8bd-3b23-40af-8b0c-871c048c1905)
![2023-10-23_14-03](https://github.com/VladimirChernyy/tileshop/assets/116533449/190955ca-3afa-4d66-93e7-836dad6c8533)
![2023-10-23_13-49](https://github.com/VladimirChernyy/tileshop/assets/116533449/6954b08e-0920-4c63-b8ad-a1e3e9c06c26)
![2023-10-23_14-01](https://github.com/VladimirChernyy/tileshop/assets/116533449/090f2957-0622-47a4-8297-f227cba9de9e)
![2023-10-23_14-02](https://github.com/VladimirChernyy/tileshop/assets/116533449/3f068153-3d17-42a2-a602-e5dd2333a18f)

## Технологии
- Python 3.10.6
- Django 4.2
- Postgresql 15.3
- Stripe
- Bootstrap
- 
## Запуск проекта
Скопируйте репазиторий

```$ git clone git@github.com:VladimirChernyy/tileshop.git```

Перейдите в директорию проекта

```$ cd tileshop```

Установите и активируйте виртуальное окружение

Linux/MacOS

```$ python3 -m venv venv```

```$ source venv/bin/activate```

Windows

```$ python -m venv env```

```$ venv\Scripts\activate.bat```

Генерируем новый секретный ключ Django

```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Создаем файл .env, в котором нужно указать данные

``` 
sudo nano .env
```
Добавьте в файл .env код  

```
DJANGO_KEY=<Сгенерированный_ключ>
POSTGRES_DB=<Желаемое_имя_базы_данных>
POSTGRES_USER=<Желаемое_имя_пользователя_базы_данных>
POSTGRES_PASSWORD=<Желаемый_пароль_пользователя_базы_данных>
DB_HOST=localhost
DB_PORT=5432
```

Установите библиотеки

```$ pip install -r requirements.txt```

Перейдите в приложение проекта

```$ cd tileshop```

Выполните миграции

Linux/MacOS

```$ python3 manage.py makemigrations```

```$ python3 manage.py migrate```

Windows

```$ python3 manage.py makemigrations```

```$ python3 manage.py migrate```

Запустите приложение

```$ python3 manage.py runserver``` для Linux/MacOS

```$ python manage.py runserver``` для Windows

Перейдите по ссылке <a href="http://localhost:8000/docs" target="_blank"> http://localhost:8000/ </a>



