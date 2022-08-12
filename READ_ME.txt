TO RUN THE DJANGO SERVER (TO BE IMPROVED):
- Pre-reqs:
  - Ability to import .tar into PostgreSQL Server
  - Django 4.0.6 (subsequently, Python)
  - Patience

1) Create a PostgreSQL database.
2) Import/Restore Backup 'django/postgreSQL/django-postgres-server.tar'
  - This should create 11 tables (auth_group, auth_group_permissions, auth_permission, auth_user, ..., nodebuilder_computer)

3) Edit django/buildtoolserver/buildtoolserver/settings.py
  - Ctrl + F: DATABASES dictionary
  - Change the following key-value pairs:
    - 'NAME': 'name-of-database'
    - 'USER': 'name-of-user'
    - 'PASSWORD': 'your-password'
    
4) In terminal, in ./django/buildtoolserver/buildtoolserver:
  - py manage.py makemigrations
  - py manage.py migrate
  - py manage.py runserver
  
5) This should create a server at 127.0.0.1:8000
