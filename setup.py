"""
Пример создания дистрибутива для UNIX - систем.

Для создания дистрибутива потребуются 3 файла: данный файл setup.py, файл с кодом example.py и README.txt
"""

from setuptools import setup


setup(
    name='example',
    version='0.1',
    description='The head first Python search Tools',
    author='Andrey',
    author_email='andrey.aslanov@gmail.com',
    url='andreqwert.github.io',
    py_modules=['vsearch'],
    )

"""
Команды для запуска в UNIX-системах:
cd <папка с кодом, файлом README.txt и этим файлом>
python3 setup.py sdist
"""
