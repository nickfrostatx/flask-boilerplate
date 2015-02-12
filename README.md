# flask-boilerplate

## Dependencies

These will be installed via `setup.py`

* Flask
* Flask-SQLAlchemy
* Flask-WTF
* py-bcrypt

## Setup

To convert this folder to your own Flask app, change the following things:

* Rename the `boilerplate` folder
* Rename in `config` folder
  * `app.py.sample`
  * `nginx.conf.sample`
* Rename in `setup.py`
  * `name='boilerplate'`
  * `packages=['boilerplate']`
  * `'boilerplate-run = boilerplate.dev:run'`
* Change the settings environment variable name in `dev.py`
* Rewrite `README.md` (so meta)

## Setting up development environment

* Create a virtualenv, and activate it
* Set BOILERPLATE_SETTINGS environment variable to config file
  * Can be achieved with `postactivate` script in virtualenvwrapper
* `pip install --editable file:/path/to/app/directory`

Create the database, then run the following command to set up tables

`boilerplate-createdb`

Now you can run the application with the following command:

`boilerplate-run`
