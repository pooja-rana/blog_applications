# Blog Applications

## Introduction
Blog Applications is a Django-based web application that allows users to create, manage, and interact with blog posts. The project is containerized using Docker, making it easy to deploy and run in different environments.

## Features
- User authentication and authorization
- CRUD operations for blog posts
- Category and tag management
- Commenting system
- PostgreSQL database integration
- Celery for asynchronous task processing
- Redis for caching and background job management

## Python Version
- **Python 3.10**

## Dependencies
The application requires the following dependencies, which are listed in `requirement.txt`:
- Django
- Psycopg2
- Celery
- Redis
- Docker

## Project Structure
```
/blog_applications
│── blog_applications/  # Main Django project folder
│   ├── settings.py  # Django settings file
│   ├── urls.py  # URL configurations
│   ├── wsgi.py  # WSGI entry point
│── user/  # User authentication and management
│── posts/  # Blog post creation, editing, and deletion
│── comments/  # Commenting system for blog posts
│── requirements.txt  # List of dependencies
│── Dockerfile  # Dockerfile for containerization
│── docker-compose.yml  # Docker Compose configuration
│── entrypoint.sh  # Script to ensure database is ready before running the app
│── manage.py  # Django's CLI management script
```

## Running the Project Locally
### 1. Environment Setup
Ensure you have the following installed:
- Python 3.10
- Docker & Docker Compose

### 2. Clone the Repository
```sh
git clone --branch develop https://github.com/pooja-rana/blog_applications.git
cd blog_applications
```
### 3️⃣ Create a Virtual Environment
```sh
$ python3 -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4️⃣ Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 5️⃣ Configure Database (MySQL/PostgreSQL)
Update `DATABASES` settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':env.str("POSTGRES_DB"),
        'USER': env.str("POSTGRES_USER"),
        'PASSWORD': env.str("POSTGRES_PASSWORD"),
        'HOST': env.str("POSTGRES_HOST"),
        'PORT': env.str("POSTGRES_PORT"),
    }
}
```

### 6️⃣ Apply Migrations
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

### 7️⃣ Create a Superuser (Admin)
```sh
$ python manage.py createsuperuser
```
Follow the prompts to set up an admin user.

### 8️⃣ Run the Development Server
```sh
$ python manage.py runserver
```
### 4. Build and Start the Application Using Docker
```sh
docker-compose up --build
```
This will:
- Build and start the Django application (`web` container)
- Start the PostgreSQL database (`db` container)
- Start Redis (`redis` container)
- Start Celery workers (`celery_worker` container)


### 4. **Create .env based on environment** :smile:
We have to create the **.env** at our project level as all the credentials and configuration will defined into **.env** file. With help of [environ](https://pypi.org/project/environs/) package python will load it and use it. this **.env** is use in docker as well. Following table contains all the configuration with optional flag, default value, docker required variables, project required variables.

| Variable Name             | Optional | Default Value                               | Docker                                 | Project                                       |
|---------------------------|----------|---------------------------------------------|----------------------------------------|-----------------------------------------------|
| POSTGRES_DB               | NO       |                                             | [Yes] in postgres container required   | [Yes] for connecting to database              |
| POSTGRES_HOST             | NO       | db                                          | [Yes] in docker db service itself host | [Yes] for connectiong to db service           |
| POSTGRES_USER             | NO       | postgres                                    | [Yes] postgres image need required     | [Yes] for connecting to database              |
| POSTGRES_PASSWORD         | NO       | postgres                                    | [Yes] postgres image need required     | [Yes] for connecting to database              |
| POSTGRES_PORT             | NO       | 5432                                        | [Yes] postgres image need required     | [Yes] for connecting to               |
| DJANGO_SUPERUSER_PASSWORD | YES      | admin                                       | [No]                                   | [Yes] `createsuperuser` commnad will use this |
| DJANGO_SUPERUSER_EMAIL    | YES      | admin@admin.com                             | [No]                                   | [Yes] `createsuperuser` commnad will use this |
| CELERY_BROKER_URL         | NO       | redis://localhost:6379/0                      | [NO]                                   | [Yes]                                         |
| CELERY_RESULT_BACKEND     | NO       | redis://localhost:6379/0                      | [NO]                                   | [Yes]                                         |
| EMAIL_BACKEND             | NO       | django.core.mail.backends.smtp.EmailBackend | [NO]                                   | [Yes]                                         | EMAIL_HOST | NO| smtp.gmail.com | [NO] | [Yes]
| EMAIL_HOST_USER           | NO       | add your email                           | [NO]                                   | [Yes]                                         |
| EMAIL_HOST_PASSWORD       | NO       | add your pass                                         | [NO]                                   | [Yes]                                         |
| EMAIL_USE_TLS             | NO       | True                                        | [NO]                                   | [Yes]                                         |
| EMAIL_PORT                | NO       | 587                                         | [NO]                                   | [Yes]                                         |
| DEFAULT_FROM_EMAIL        | NO       | EMAIL_HOST_USER                             | [NO]                                   | [Yes]                                         |
