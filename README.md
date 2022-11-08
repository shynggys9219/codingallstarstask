# DRF APP REST API приложение -сервис для управления виртуальными серверами (VPS).


## Содержание
- [Tastk](#task)
- [Технологии](#технологии)
- [Использование](#использование)
- [Требования](#требования)
- [Установка зависимостей](#установка-зависимостей)
- [Done by](#done-by)

## Task 

### To create a scraper to get data from coursera.org
https://docs.google.com/document/d/1f_wMDAndEK5zU3BXpQhGnjOMyKx5aX3YL3UKKSnqF2c/edit

### API поддерживает операции
- создать VPS
- получить VPS по uid
- получить список VPS с возможностью фильтрации по параметрам
- перевести VPS в другой статус

## Технологии
- [Django](https://djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

## Использование
Установите библиотеки из - [Требования](#требования):
Далее перейдите в папку, где есть main.py и наберите следующую команду:
- bash/terminal
```sh
$ python3 manage.py runserver
```
- cmd
```cmd
> python manage.py runserver
```


## Требования
Для установки и запуска проекта, необходимы 
- Django
- Django Filters
- Django Rest Framework

## Установка зависимостей
Для установки зависимостей, выполните команды в cmd или bash/terminal:
```cmd
> pip install django==4.0.2
> pip install django-filter==21.1
> pip install djangorestframework==3.13.1
```

```sh
$ pip3 install django==4.0.2
$ pip3 install django-filter==21.1
$ pip3 install djangorestframework==3.13.1
```

## Запуск Development сервера
Чтобы запустить сервер для разработки, выполните команду в cmd или bash/terminal:
```cmd
> python manage.py runserver
```
```sh
python3 manage.py runserver
```


## Тестирование
Был использован нативный класс из DRF APITestCase
```cmd
> python manage.py test
```
```sh
python3 manage.py test
```

## Done by
- [Shynggys Alshynov](https://www.linkedin.com/in/alshynov-shynggys-532576195/) — Backend Dev
