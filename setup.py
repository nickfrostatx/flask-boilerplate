from setuptools import setup

setup(
    name='flask-boilerplate',
    version='0.1.0',
    packages=['boilerplate'],
    install_requires=[
        'Flask>=0.10.1',
        'Flask-SQLAlchemy>=2.0',
        'Flask-WTF>=0.11',
        'py-bcrypt>=0.4',
    ],
    entry_points={
        'console_scripts': [
            'boilerplate-createdb = boilerplate.dev:createdb',
            'boilerplate-run = boilerplate.dev:run',
        ],
    },
)
