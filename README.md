# Django Application to scrape data from coursera, save it as csv and download if needed.


## Content
- [Task](#task)
- [Techs](#techs)
- [Usage](#usage)
- [Requirements](#requirements)
- [Done by](#done-by)

## Task 

### To create a scraper to get data from coursera.org
https://docs.google.com/document/d/1f_wMDAndEK5zU3BXpQhGnjOMyKx5aX3YL3UKKSnqF2c/edit

## Techs
- [Django](https://djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Asyncio](https://pypi.org/project/asyncio/)
- [Pandas](https://pypi.org/project/pandas/)
- [aiolimiter](https://pypi.org/project/aiolimiter/)
- [BeutifulSoup4](https://pypi.org/project/bs4/)

## Usage
In order to everything to work properly please install these requirements - [Requirements](#requirements):
If you already installed libraries from requirements then follow to the project folder (where manage.py is located) and run one of commands below:
- bash/terminal
```sh
$ python3 manage.py runserver
```
- cmd
```cmd
> python manage.py runserver
```
- Once you have started the server please go to http://127.0.0.1:8000/ on your browser.

## Requirements
To run this project you need to install these libraries using command: 
- bash/terminal
```sh
$ pip3 install library_name==version
```
- cmd
```cmd
> pip install library_name==version
```
- Django==4.0.2
- django-cors-headers==3.11.0
- django-filter==21.1
- aiolimiter==1.0.0
- beautifulsoup4==4.11.1
- httpx==0.23.0
- pandas==1.4.2

## Done by
- [Shynggys Alshynov](https://www.linkedin.com/in/alshynov-shynggys-532576195/) — Backend Dev
