This read-me is composed of several parts:
- Project Overview
- How to run the Django Server


PROJECT OVERVIEW:
Hacknet is a terminal-based hacking simulator released on Steam in 2015, where the player is tasked with hacking into various different computers and servers using pseudo-UNIX commands.

It can be purchased here:
https://store.steampowered.com/app/365450/Hacknet/

The game allows for players to create their own stories in-engine, called 'Extensions', through the use of .xml files, with specific elements and tags.

An Example Computer Node can be found here:
https://pastebin.com/NwtgTdPW

Hacknet-Ext-BuildTool makes a form-fillable UI, which allows users to:
- Create in-game objects
- assign various different properties to them
- save said objects to database
- and generate the subsequent .xml documents.

It runs on the Django Full-stack (Javascript -> Python -> Django -> PostgreSQL)


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
    
4) In terminal, in ./django/buildtoolserver:
  - py manage.py makemigrations
  - py manage.py migrate
  - py manage.py runserver
  
5) This should allow you to connect to the web server at 127.0.0.1:8000
  - specifically, go to 127.0.0.1:8000/nodes


Special thanks to Fayti1703 and the Hacknet Extensions discord community for all their help in understanding these files
