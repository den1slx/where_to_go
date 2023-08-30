# Афиша

### О проекте

Сайт с картой с интересных мест.  
[Ссылка на сайт](https://denislx.pythonanywhere.com/), [Ссылка на админку](https://denislx.pythonanywhere.com/admin/),
[Источник]().


### Установка
- python3 должен быть установлен.
- Скачайте код.
- Установите зависимости командой:
```commandline
pip install -r requirements.txt
```

### Использование
* Перейдите в директорию с файлом manage.py
```commandline
cd your\path\to\project\projectname
```

* Добавление администратора
```commandline
python manage.py createsuperuser
```
* Запуск
```commandline
python manage.py runserver
```
* Загрузка из `json` файла
  * Для загрузки из локального файла
  ```commandline
  python manage.py load_place 'pathtolockalfile'
  ```
  * Для `url`
  ```commandline
  python manage.py load_place 'url' -u
  ```
  тестовый url: https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json
  * Для информации
  ```commandline
    python manage.py load_place -h
  ```
* Сайт будет находиться [здесь](http://127.0.0.1:8000/)
* Админка будет находиться [здесь](http://127.0.0.1:8000/admin)

#### структура DB
* Place
    * title - char 200
    * description_short - TextField
    * lng - float
    * lat - float
    * description_long - HTMLField
* PlaceImage
    * image - image
    * place - FK Place
    * ordering - for ordering

#### Окружение

* SECRET_KEY=yoursecretkey
* DEBUG=False (default=True)
* DATABASE_ENGINE=django.db.backends.sqlite3
* DATABASE_NAME=db.sqlite3
* SESSION_COOKIE_SECURE=True (default=False)
* CSRF_COOKIE_SECURE=True (default=False)
* SECURE_SSL_REDIRECT=True (default=False)
* ALLOWED_HOSTS=yourhost1,yourhost2,etc  
* STATIC_ROOT=assets (default=static)

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).