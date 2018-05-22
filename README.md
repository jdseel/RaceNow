# This is Jonathan Seel's RaceNow App Repo
RaceNow is an easy way to quickly create and manage events for races.
It simply allows the user to create a race and add all the events for that race.

The database setup for this project is as follows:

Races Table | Type/Relationship
------------ | -------------
ID | Int Unique Key
Name | Text
Location | Text
Name | Text
Type | Text
About | Text

Events Table | Type/Relationship
------------ | -------------
ID | Int Unique Key
Name | Text
Event Type | Text
Age Level | Text
Race | Text Foreign Key from Races Table
Results | Text


To run this website with python:

Install virtualenv if needed.

If you do not have a virtual environment yet on the project folder, set it up with:

    $ virtualenv venv

Then activate the virtual environment

    $ source venv/bin/activate

Install packages

    $ pip install -r requirements.txt

To initialize the database:

    $ python manage.py deploy

To run the development server (use -d to enable debugger and reloader):

    $ python manage.py runserver -d
