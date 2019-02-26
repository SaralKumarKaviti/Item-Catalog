# Item-Catalog

## By Saral Kumar Kaviti

This web application is a project for the Udacity [FSND Course](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## About Project

This Project is a RESTful web application utilizing the Flask Framework which accesses a SQL database that populates cricket country categories and their cricket players information. OAuth2 provides authentication for furuther CRUD functionality on the application. Currently OAunt2 is implemented for Google Accounts.

## In This Project

This project has one main python module `cricket.py` which runs the flask application. A SQL database is created using the `cricket_database.py` module and you can populate the database with test data using `cricket_player_info.py`

The Flask application uses stored HTML templates in the templates directory to build the front-end of application.

## Software Requirements

* Python3
* VirtualBox
* Vagrant
* Git
* SQLite DB
* Text Editor(Sublime Text3)

## Required Skills

* Python3
* HTML
* CSS
* Bootstrap
* OAuth
* Flask Framework
* sqlalchemy

## Features

* Authentication and authorisation check
* Full CRUD support using SQLAlchemy and Flask
* JSON endpoints.
* Implements oAuth using Google Sign-in API

## Installation
There are some dependancies and few instructions on hoee to run the application. Seperate instructions are provided to get GConnect working also.

## URL's

- [Git](https://git-scm.com/downloads)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/)
- [Vagrantfile](https://https://github.com/udacity/fullstack-nanodegree-vm)
- [Sublime Text](https://www.sublimetext.com/3)

## Installation Process

* Install Git, Sublime text, VirtualBox and Vagrant
* Clone the Udacity Vagrantfile
* Goto Vagrant dictory and download the zip file and place here 
* Open terminal or git
* Launch the Vagrant VM(`vagrant up`)
* Run Vagrant VM(`vagrant ssh`)
* Now change the directory into vagrant folder i.e., `cd /vagrant`
* The application imports requests which is not on this vm. Run pip install requests

## Some dependencies libraries

* pip install Flask
* pip install sqlalchemy
* pip install requests
* pip install psycopg2
* pip install oauth2client

## How to run python files

- Here we are creating three different files
	
	* cricket_database.py - It is a database file. In this database files i have created country and player tables.

	* cricket_player_info.py - In this file we are inserting sample data.

	* cricket.py - It is main file for running application.

- Now open git or terminal and inside project folder type python filename.py, 
	1. python cricket_database.py
	2. python cricket_player_info.py
	3. python cricket.py

## Using Google Login
To get the Google login working there are a few additional steps:

1. Goto [Google Dev Console](https://console.developers.google.com)
2. Login if prompted
3. Goto Credentials
4. Select Create Credentials
5. Select OAuth Client ID
6. Select Web Application Name
7. Enter Application Name 'Cricket Player Item-catalog'
8. Authorized JavaScript origins = 'http://localhost:5050'
9. Authorized redirect URLs = 'http://localhost:5050/login' && 'http://localhost:5050/gconnect'
10. Select Create
11. Select Create ID and Paste it into the `data-clientID` in login.html
12. On the Dev Console Select and Download JSON
13. Rename JSON file to client_secrets.json 
14. Place JSON file in item-catalog directory that you 
15. Run application using `python /item-catalog/cricket.py`

## JSON Endpoints

The following are open to the public:

Country Catalog JSON: `localhost:5050/country/JSON'`
	
	- It displays the whole country catalog. Country categories and all players.

Playerwise JSON: `localhost:5050/country/<int:player_id>/menu/JSON`

    - Based on player id it  will displays the particular country player.

Country of particular player details JSON: `localhost:5050/country/<int:country_id>/menu/<int:player_id>/JSON`

    - it displays the particular country of particulr player information.


## Miscellaneous

This project is inspiration from [gmawji](https://github.com/gmawji/item-catalog).
