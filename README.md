[![Build Status](https://github.com/ArslanYadov/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)](https://github.com/ArslanYadov/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

# Foodgram
_место-для-слогана_
### Request
``` bash
$ curl http://localhost:8000/api/recipes/
```
### Response
``` json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results":  [
        {
            "id": 1,
            "tags": [
                {
                    "id": 2,
                    "name": "Обед",
                    "color": "#49B64E",
                    "slug": "lunch"
                }
            ],
            "author": {
                "email": "vpupkin@yandex.ru",
                "id": 1,
                "username": "vasya.pupkin",
                "first_name": "Вася",
                "last_name": "Пупкин",
                "is_subscribed": false
            },
            "ingredients": [
                {
                    "id": 1916,
                    "name": "фарш (свинина и курица)",
                    "measurement_unit": "г",
                    "amount": 500
                },
                {
                    "id": 886,
                    "name": "лук репчатый",
                    "measurement_unit": "г",
                    "amount": 100
                }
            ],
            "is_favorited": false,
            "is_in_shopping_cart": false,
            "name": "Котлета по киевски",
            "image": "http://localhost:8000/media/recipes/images/temp.png",
            "text": "Рецепт приготовления котлеты по киевски.",
            "cooking_time": 40
        }
    ]
}
```
### Описание
* **Foodgram** - это сервис для тех, кто любит готовить,
постоянно ищет новые рецепты и вдохновение,
и хочет делиться своими рецептами с другими. 

* **Foodgram** позволяет подбирать новые рецепты по параметрам (например только завтраки по тэгу _breakfast_), 
добавлять лучшие рецепты в избранные,
а на любимых авторов можно подписаться, чтобы не пропускать новые рецепты.

* Планируй свои покупки с помощью сервиса: 
добавляй рецепты в покупки, формируя единый список со всеми необходимыми ингредиентами и их количеством, 
скачивай его в текстовом формате и отправляйся в магазин. 
Больше не нужно считать вес и количество одинаковых продуктов из разных рецептов вручную: все рассчитывается автоматически.
### Возможности по пользовательским ролям
* Любой Гость может просматривать все доступные рецепты, применять фильтрацию по _тэгам_.
* Зарегестрированный пользователь может: 
    1. Создавать/обновлять свои собственные рецепты;
    2. Добавлять рецепты других авторов в избранное или удалять их оттуда;
    3. Подписываться на авторов других рецептов;
    4. Добавлять/удалять рецепты в список покупок и скачивать необходимые для покупки ингредиенты.
### Технологии
* [Python 3.10.6](https://docs.python.org/3.10/)
* [Django 4.1.4](https://docs.djangoproject.com/en/4.1/) + [REST](https://www.django-rest-framework.org/)
## Запуск проекта на данный момент
- В `settings.py` раскомментить нужную БД. (сейчас для дебага используется _sqlite_)
- Добавить в свой файл с переменными окружения `.env` значения переменных по примеру из файла `.env.template`
- Воспользоваться командой `make setup` из файла **Makefile** для сбора и запуска проекта на локальном сервере
``` bash
$ make setup
```
## Автор бэкенда
Арслан Ядов

E-mail:
[Arslan Yadov](mailto:arslanyadov@yandex.ru?subject=foodgram%20diplom%20project)
