# Trial Task Assignment
This project is a Django application that allows users to upload files, which are then encrypted using Fernet and then saved to the server.

# Pre-requisites

- Python 3.7 or higher
- Django 5.1.1 or higher
- Django REST Framework
- Cryptography

# Project Structure

```
file_encryption_project/
    manage.py
    file_encryption_project/
        __init__.py
        settings.py
        urls.py
    file_encrypter/
        __init__.py
        admin.py
        apps.py
        models.py
        urls.py
        views.py
    media/                     # Directory where encrypted files are saved
    requirements.txt           # Project dependencies
    README.md                  # This file
```

# Getting started

- Clone the repository

```
git clone https://github.com/TanV060892/file_encryption_project.git
cd file_encryption_project
```

- Install dependencies

```
pip install -r requirements.txt
```

- Create Required Directories

```
mkdir media

```

- Build and run the project

```
On Windows :
python -m venv venv
.\venv\Scripts\activate
python manage.py migrate
python manage.py runserver
```

- Health Check

  Endpoint : http://127.0.0.1:8000

## API Documentation

```
https://documenter.getpostman.com/view/29641974/2sAXqs7hoM

```

- `POST /api/upload/` - Upload a file to be encrypted and need to store on server

```
Request
    Form-Data:
        Key: file
        Value: File to upload

Response
    Success:
        {
            "status": true,
            "data": {
                "message": "File uploaded and encrypted successfully",
                "encryption_key": "<encryption_key>",
                "file_path": "<file_path>"
            }
        }
    
    Error:
        {
            "status": false,
            "error": {
                "code": "OTZ400",
                "message": "No file uploaded"
            }
        }
```

## Testing

```
python manage.py test
```

## Additional Notes

- Ensure that the MEDIA_ROOT setting in settings.py is configured correctly.
- The encryption key should be stored securely and not exposed in production environments.
