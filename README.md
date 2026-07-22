1.  Install prerequisites
 Install Python 3.11 or below (same version used for the project)
 Install MySQL Server
 Install Git
 Install VS Code (optional)
 Install MySQL Workbench (optional)
2.  Clone the project
3.  Create virtual environment
    python3 -m venv env
    source env/bin/activate
4.  Install Python packages
5.  Start MySQL
6.  Create database
7.  Configure database
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "company",
            "USER": "root", (adjustable)
            "PASSWORD": "", (adjustable)
            "HOST": "localhost",
            "PORT": "3306",
        }
    }
8.  Apply migrations
    python manage.py makemigrations
    python manage.py migrate
9.  Import Thailand location data
10. Create superuser (if needed)
11. Run development server
    python manage.py runserver 0.0.0.0:8000
12. Open Admin
13. Add data
14. Print labels