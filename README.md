# Cebu city site
News source project with Django

## Check it out!
[News project deployed to Render](https://cebusite.onrender.com/)

## Demo User Test

* login: DemoUser
* password: Test12345

## Installation

1. git clone https://github.com/IvanGLS/cebu_news
2. python -m venv venv
3. venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py runserver

## Env variables configuration
* db_from_env - PostgreSQL database settings
* DROPBOX_OAUTH2_TOKEN - settings from dropbox.com
* DROPBOX_APP_KEY - settings from dropbox.com
* DROPBOX_APP_SECRET - settings from dropbox.com
* DROPBOX_OAUTH2_REFRESH_TOKEN - settings from dropbox.com for host images

## Features

* Authentication functionality for Redactor/User
* Managing news directly from website
* Powerful admin panel for advanced managing

## Demo
Home Page
![Website home page](static/images/demo_images/demo-home.png)

Redactor's Page
![Website home page](static/images/demo_images/demo-user.png)

News Detail Page
![Website home page](static/images/demo_images/demo-detail.png)

Project homepage: https://github.com/IvanGLS/cebu_news
Repository: https://github.com/IvanGLS/cebu_news