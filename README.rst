django-receipts
===============

This is the sample code used in the Real Python article `How to Write an
Installable Django App <https://realpython.com/installable-django-app/>`_. The
article describes how to take an app from an existing Django project and make
it a stand-alone installable package available on PyPI.

Installable App
---------------

This app models a list of items on a receipt. Each item has a description and a cost. A receipt may reference multiple items.

This app can be installed and used in your Django project with:

.. code-block:: bash

    $ pip install realpython-django-receipts


Edit your `settings.py` file to include `'receipts'` in the `INSTALLED_APPS`
listing.

.. code-block:: python

    INSTALLED_APPS = [
        ...

        'receipts',
    ]


Edit your project `urls.py` file to import the URLs:


.. code-block:: python

    url_patterns = [
        ...

        path('receipts/', include('receipts.urls')),
    ]


Finally, add the models to your database:


.. code-block:: bash

    $ ./manage.py makemigrations receipts


The "before" project
--------------------

The `before folder <https://github.com/realpython/django-receipts/000_before>`_ shows the "before" case -- the Django project before the app was made installable.


Docs & Source
-------------

* Article: https://realpython.com/installable-django-app/
* Source: https://github.com/realpython/django-receipts
* PyPI: https://pypi.org/project/realpython-django-receipts/
