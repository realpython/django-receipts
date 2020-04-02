# django-receipts

This is sample code used in the Real Python article [Writing an Installable Django App](???). The article describes how to take an app from an existing Django project and make it a stand-alone installable package avilable on PyPI.

## Installable App

This app models a list of items on a receipt. Each item has a description and a cost. A receipt may reference multiple items.

This app can be installed and used in your django project by:

```console
$ pip install realpython-django-receipts
```

Edit your `settings.py` file to include `'receipts'` in the `INSTALLED_APPS`
listing.

```python
INSTALLED_APPS = [
    ...

    'receipts',
]
```

Edit your project `urls.py` file to import the URLs:

```python
url_patterns = [
    ...

    path('receipts/', include('receipts.urls')),
]
```

Finally, add the models to your database:

```console
$ ./manage.py makemigrations receipts
```

## The "project" Branch

The [master branch](https://github.com/realpython/django-receipts/tree/master) contains the final code for the PyPI package. There is also a [project branch](https://github.com/realpython/django-receipts/tree/project) which shows the "before" case -- the Django project before the app has been removed.

## Docs & Source

* Article: ???
* Source: https://github.com/realpython/django-receipts
* PyPI: ???
