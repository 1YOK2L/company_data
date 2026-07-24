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
6.  Create unique database name and grant permissions
    wp7415@1YOK2 company_data % mysql -u root
    mysql> CREATE DATABASE name_field_from_settings_py;
    Query OK, 1 row affected (0.008 sec)

    mysql> GRANT ALL PRIVILEGES ON name_field_from_settings_py.* TO 'user_field_from_settings_py'@'localhost';
    Query OK, 0 rows affected (0.007 sec)

    mysql> 
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
9.  Import Thailand location data (location, subdistrict, district, province, zip code)
10. Create superuser (if needed)
11. Run development server
    python manage.py runserver 0.0.0.0:8000
12. Open Admin
13. Add data
14. Print labels