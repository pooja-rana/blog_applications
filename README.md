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

MIT License

