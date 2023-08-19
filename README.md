# Афиша

### О проекте

Сайт с картой с интересных мест.  
[Ссылка на сайт](), [Ссылка на админку](),
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
* Сайт будет находиться [здесь](http://127.0.0.1:8000/)
* Админка будет находиться [здесь](http://127.0.0.1:8000/admin)

#### структура DB
* Place
    * title - char 200
    * description_short - char 350
    * lng - float
    * lat - float
    * description_long - HTMLField
* PlaceImage
    * image - image
    * place - FK Place
    * my_order - for ordering



### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).