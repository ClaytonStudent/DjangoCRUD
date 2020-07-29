# DjangoCRUD
Python Django project for implementing CRUD operation.

### Introduction

We will create a simple app to store, edit and delete information.

Download/Clone repository and run following commands:

- Create Django CRUD project:

```
django-admin startproject employee_project
```

- In project directory, create application:

```
python manage.py startapp employee_register
```

- Define model in /employee_register/models.py
- Create and define form /employee_register/forms.py
- Create edit, index and show view in /employee_register/templates/
- Define urls in /employee_register/urls.py
- Add 'employee_register' app to main app in /employee_project/settings.py
- Migrate Models:

```
python manage.py migrate
```

- Run server:

```
python manage.py runserver
```

### Project structure

```
* Django_CRUD/
  |--- employee_project/
  |    |--- employee_register/
  |    |    |--- migrations/
  |    |    |--- templates/remployee_register/
  |    |    |    |--- base.html
  |    |    |    |--- employee_form.html
  |    |    |    |--- employee_list.html
  |    |    |--- admin.py
  |    |    |--- apps.py
  |    |    |--- forms.py
  |    |    |--- models.py
  |    |    |--- tests.py
  |    |    |--- urls.py
  |    |    |--- views.py
  |    |--- employee_project/
  |    |    |--- __init__.py
  |    |    |--- settings.py
  |    |    |--- urls.py
  |    |    |--- wsgi.py
  |    |--- manage.py
  |--- venv/
```

