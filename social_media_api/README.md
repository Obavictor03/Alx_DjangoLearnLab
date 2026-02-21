# Social Media API — Authentication & Accounts Module

## 📌 Overview

This project implements a user authentication system for a social media API using Django and Django REST Framework.

Features include:

* Custom user model extending Django’s AbstractUser
* User registration
* Token-based authentication
* Login endpoint
* User profile management
* Follow system foundation (followers field)

---

## 🧱 User Model Overview

The project uses a custom user model to support social media features.

Key fields:

* **username** — Unique identifier for login
* **email** — User email address
* **password** — Securely hashed password
* **bio** — Short user description
* **profile_picture** — Optional image upload
* **followers** — Self-referencing ManyToMany field to track followers

The followers field is asymmetrical, allowing one-way relationships (User A can follow User B without B following A).

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd social_media_api
```

---

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If Pillow is not included:

```bash
pip install Pillow
```

---

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### 6. Run Development Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication System

The API uses Django REST Framework Token Authentication.

After successful registration or login, a token is returned and must be included in subsequent requests.

### Authorization Header Format

```
Authorization: Token <your_token>
```

---

## 🌐 API Endpoints

Base URL:

```
/api/accounts/
```

---

### 📝 Register User

**Endpoint**

```
POST /api/accounts/register/
```

**Request Body**

```json
{
  "username": "victor",
  "email": "victor@email.com",
  "password": "securepassword",
  "bio": "Backend developer"
}
```

**Response**

```json
{
  "user": {
    "id": 1,
    "username": "victor",
    "email": "victor@email.com",
    "bio": "Backend developer",
    "profile_picture": null
  },
  "token": "abc123xyz"
}
```

---

### 🔑 Login

**Endpoint**

```
POST /api/accounts/login/
```

**Request Body**

```json
{
  "username": "victor",
  "password": "securepassword"
}
```

**Response**

```json
{
  "token": "abc123xyz"
}
```

---

### 👤 User Profile

Requires authentication.

**Endpoint**

```
GET /api/accounts/profile/
```

**Headers**

```
Authorization: Token <your_token>
```

**Response**

```json
{
  "id": 1,
  "username": "victor",
  "email": "victor@email.com",
  "bio": "Backend developer",
  "profile_picture": null
}
```

---

### ✏️ Update Profile

```
PATCH /api/accounts/profile/
```

Example body:

```json
{
  "bio": "Senior backend developer"
}
```

---

## 📁 Project Structure (Accounts App)

```
accounts/
├── models.py        # Custom user model
├── serializers.py   # DRF serializers
├── views.py         # API views
├── urls.py          # Route definitions
```

---

## 🔒 Security Notes

* Passwords are hashed using Django’s built-in authentication system
* Tokens must be kept secure
* Unauthorized requests will be rejected

---

## 🚀 Future Enhancements

Planned features for the full social media API:

* Follow / Unfollow endpoints
* Posts and comments system
* Likes and reactions
* Media uploads
* Notifications
* JWT authentication support

---

## 📄 License

This project is for educational purposes.
