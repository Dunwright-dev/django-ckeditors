.. TODO: Add codespell to linting checks

============
Contributing
============

How to Contribute
=================

We love it when you find problems or suggest changes!

Things to Think About
---------------------

#. Small Changes: We like small fixes best. It's easier for us to check them out and say "yes."
#. Fixing Problems: If you fix something that's broken, we'll look at it sooner.
#. New to This? Check out this guide if you've never made a change like this before: [GitHub guide][submit-a-pr]

Let's Get Started
-----------------

#. Fork the Repository: Create your personal copy of the project's code repository.
#. Clone Your Fork: Download your forked repository to your local machine.
#. Create a Branch: Start a new branch for your changes.

.. important::

   Always create a new branch before making changes. This keeps your work separate and prevents accidental overwrites to the main branch.


Formatting and Linting
----------------------



Python Code
~~~~~~~~~~~

.. important:: Ruff Formatting
   Currently, the Ruff formatter does not sort imports. In order to both sort imports and format, call the Ruff linter and then the formatter:

   ```bash
   ruff check --select I --fix
   ruff format
   ```

Testing
=======

### Installation

#### Virtual Environment

Create a virtual environment, any of [py37 - py3.12] is required.

Instal the depencencies.  These are stored in pyproject.toml in the root folder.

```bash

pip install .
pip install .[dev]

```
When working making changes to django-ckeditors its advisable to install the library 
into the venv in editable mode.

This allows you to make changes and test as you go without the need to deploy it.

```bash
pip install -e /absolute/path/to/django_ckeditors
```

#### Webpack

You will need [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed and then follow the installation guide for [Webpack](https://webpack.js.org/guides/installation/)


#### Building the js files.

You will need to change to `django-ckeditors/django_ckeditors` directory and build the `js bundle`.

```bash
npm run dev
```

or for a smaller `js bundle`

```bash
npm run prod
```

:::{admonition} JS Assets
:class: 
Each time you make a change to any of the  `js` or `css` files you will need to
build your `js` assetts.
:::

### Run the template's test suite

To run the tests of the template using the current Python version:

```bash
$ tox -e py
```

This uses `pytest `under the hood, and you can pass options to it after a `--`. So to run a particular test:

```bash
$ tox -e py -- -k test_default_configuration
```

For further information, please consult the [pytest usage docs](https://pytest.org/en/latest/how-to/usage.html#specifying-which-tests-to-run).

### Run the generated project tests

The template tests are checking that the generated project is fully rendered and that it passes `flake8`. We also have some test scripts which generate a specific project combination, install the dependencies, run the tests of the generated project, install FE dependencies and generate the docs. They will install the template dependencies, so make sure you create and activate a virtual environment first.

```bash
$ python -m venv venv
$ source venv/bin/activate
```

These tests are slower and can be run with or without Docker:

- Without Docker: `tests/test_bare.sh` (for bare metal)
- With Docker: `tests/test_docker.sh`

All arguments to these scripts will be passed to the `cookiecutter` CLI, letting you set options, for example:

```bash
$ tests/test_bare.sh use_celery=y
```

## Submitting a pull request

Once you're happy with your changes and they look ok locally, push and send send [a pull request][submit-a-pr] to the main repo, which will trigger the tests on GitHub actions. If they fail, try to fix them. A maintainer should take a look at your change and give you feedback or merge it.

[submit-a-pr]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request


