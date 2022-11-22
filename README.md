# WishIt

Simple webapplication to manage and share presonal wishes

### REQUIREMENTS

* Docker
* Django Installation
* PostgreSQL Container / Installation
  * python manage.py makemigrations
  * python manage.py migrate

### Getting Started

1. Create /wishit/.env File and modify content
2. run "docker-compose build"
3. run "docker-compose up"

Lokal:

python manage.py runserver

### Structure

/wishit contains main configuration

/externalAuth contains domain for authentication with external identification provider

/internalAuth contains domain for registration, login, ...

/wishManagement contains domain for lists and wishes

/priceComparison contains domain for external price comparison
