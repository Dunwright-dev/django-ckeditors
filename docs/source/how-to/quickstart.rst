.. include:: ../../extras.rst.txt
.. highlight:: rst
.. index:: how-to-quickstart ; Index


.. _how-to-quickstart:

===========================
django-ckeditors Quickstart
===========================

Introduction
------------

django-ckeditors is a powerful Django application that seamlessly integrates the rich text editor CKEditor into your projects. This guide will walk you through the installation and basic usage.

Prerequisites

    A working Django project

    Basic familiarity with Python and Django concepts


Installation
------------

1. **Install the package:**

   .. code-block:: bash

      pip install django-ckeditors

Configuration
-------------

1. **Add to `INSTALLED_APPS`:**

   .. code-block:: python

      INSTALLED_APPS = [
          ...  # Your existing apps
          'django_ckeditors',
      ]


2. **Update your `settings.py`:**

   .. code-block:: python

      STATIC_URL = '/static/'
      MEDIA_URL = '/media/'
      MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

      CKEDITORS_CONFIGS = {
          'default': {
              'toolbar': 'full',  # Customize as needed (see below)
          },
      }

3. **Add URLs to your `urls.py`**

   .. code-block:: python

      from django.conf import settings
      from django.conf.urls.static import static

      urlpatterns = [
          # ... your existing URLs
          path("ckeditor5/", include('django_ckeditors.urls'), name="ck_editors_upload_file"),
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Using the Editor
----------------

1. **In a Model:**

   .. code-block:: python

      from django.db import models
      from django_ckeditors.fields import CKEditorsField

      class Article(models.Model):
          title = models.CharField('Title', max_length=200)
          text = CKEditorsField('Text')  # Use the Rich Text Field!

2. **In a Form:**

   .. code-block:: python

        from django import forms
        from django_ckeditors.widgets import CKEditorsWidget
        from .models import Article

        class ArticleForm(forms.ModelForm):
            class Meta:
                model = Article
                fields = ['title', 'text']
                widgets = {
                    'text': CKEditorsWidget()
                }

3. **In a Template:**

   .. code-block:: html

        {% extends 'base.html' %}

        {% block content %}
          <form method="POST">
            {{ form.media }}  # Dont forget this line.
            {% csrf_token %}
            {{ form.as_p }}
           <button type="submit">Submit</button>
         </form>
        {% endblock content %}


Customization
-------------

* **Toolbar:** Edit the `toolbar` option in `CKEDITORS_CONFIGS` to select your desired buttons. Refer to the CKEditor 5 documentation for customization options: https://ckeditor.com/docs/ckeditor5/latest/features/index.html.

* **CSS Styling:** Share styles between the editor and your website by using the `content-styles.css` from CKEditor 5. Refer to the CKEditor 5 documentation for customization options: https://ckeditor.com/docs/ckeditor5/latest/installation/advanced/content-styles.html#sharing-content-styles-between-frontend-and-backend .


Making Your Django Website Multilingual with CKEditor
-----------------------------------------------------

Do you want your website to automatically adapt to the language your visitors use? Here's how to easily achieve this with Django and CKEditor:

1. Enable Language Detection in Your Settings

* Open your Django project's settings.py file.

* Add the following line:

 .. code-block:: python

    CKEDITOR_USER_LANGUAGE = True

* This tells CKEditor to detect the user's browser language and adjust the editor's interface accordingly.

2. Specify Supported Languages

* You'll need to tell CKEditor which languages you want to support. This is usually done in your CKEditor configuration ("as shown below"):

.. tip::

    You can specify the desired language(s) for your website's interface and content in the following formats:

    +------------------------+-------------------------------------------------------+----------------------------------+
    | Option                 | Description                                           | Example                          |
    +========================+=======================================================+==================================+
    | Single language string | Specifies a single language for the entire UI         |  "fr"                            |
    +------------------------+-------------------------------------------------------+----------------------------------+
    | List of languages      | Provides a prioritized list for content display       | ["de", "en", "fr"]               |
    +------------------------+-------------------------------------------------------+----------------------------------+
    | Dictionary             | Sets the primary UI language, with optional fallbacks | {"ui": "es", "fallback": ["en"]} |
    +------------------------+-------------------------------------------------------+----------------------------------+


.. code-block:: javascript

    CKEDITOR.config.language = 'en'; // English by default
    CKEDITOR.config.language_list = [
        'en', 'fr', 'es', // Add the language codes you support
    ];


**Key Points:**

    **Language Codes:** Use standard language codes like 'en' for English, 'fr' for French, etc.

    **Translation:** This setup only changes the CKEditor interface language. You'll still need to handle the actual translation of your website content. Django has excellent internationalization support for that.
