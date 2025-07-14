# 📝 BlogAPI - Secure Blogging Platform (Backend)

A RESTful backend API built with Django REST Framework (DRF) for user-authenticated blogging.

## 🔧 Features

- User registration & login using JWT
- Create posts tied to logged-in users
- View all posts (public)
- View only logged-in user's posts
- Delete only your own posts
- Class-based views using DRF
- Token-based authentication

## 🛠 Tech Stack

- Python 3.10
- Django 5.x
- Django REST Framework
- Simple JWT

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/<your-username>/blogapi.git
cd blogapi

# Create virtual env and activate
python -m venv venv
venv\Scripts\activate  # on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run server
python manage.py runserver
