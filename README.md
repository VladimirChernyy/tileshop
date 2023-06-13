# Онлайн магазин 
### Описание
Магазин продажи инструмента и расходных материалов для обработки керамогранита
### Технологии
- Python 3.10.6
- Django 4.2
- Postgresql 15.3
### Запуск проекта
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

Перейдите по ссылке <a href="http://localhost:8010/docs" target="_blank"> http://localhost:8000/ </a>



