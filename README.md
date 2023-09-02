# Афиша

### О проекте

Сайт с картой с интересных мест.  
[Ссылка на сайт](https://denislx.pythonanywhere.com/), [Ссылка на админку](https://denislx.pythonanywhere.com/admin/),
[Источник]().


### Установка
- python3 должен быть установлен. (3.10.11)
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

* SECRET_KEY=yoursecretkey  [docs](https://docs.djangoproject.com/en/4.2/ref/settings/#secret-key)
* DEBUG=False (default=True)  [docs](https://docs.djangoproject.com/en/4.2/ref/settings/#debug)
* DATABASE_ENGINE=your db engine (default='django.db.backends.sqlite3') [docs](https://docs.djangoproject.com/en/4.2/ref/settings/#engine)
* DATABASE_NAME=your db (default='db.sqlite3')  [docs](https://docs.djangoproject.com/en/4.2/ref/settings/#name)
* SESSION_COOKIE_SECURE=True (default=False)  [docs](https://docs.djangoproject.com/en/4.2/ref/settings/#session-cookie-secure)
* CSRF_COOKIE_SECURE=True (default=False)  [docs](https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-cookie-secure)
* SECURE_SSL_REDIRECT=True (default=False)  [docs](https://docs.djangoproject.com/en/4.2/ref/settings/#secure-ssl-redirect)
* ALLOWED_HOSTS=yourhost1,yourhost2,etc  (default=['127.0.0.1', '.localhost'])  [docs](https://docs.djangoproject.com/en/4.2/ref/settings/#allowed-hosts)
* STATIC_ROOT=assets (default=static)  [docs](https://docs.djangoproject.com/en/4.2/ref/settings/#static-root)

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).