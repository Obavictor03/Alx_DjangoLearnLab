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

## Posts & Comments
Base URL
http://localhost:8000/api/
1️⃣ Posts Endpoints
List Posts

URL: /posts/

Method: GET

Description: Retrieve a paginated list of posts. Supports searching by title or content.

Query Parameters:

Parameter	Type	Description
page	int	Page number (for pagination)
page_size	int	Number of posts per page (max 50)
search	string	Search posts by title or content

Example Request:

GET /api/posts/?page=1&page_size=5&search=django
Authorization: Token <user-token>

Example Response:

{
    "count": 12,
    "next": "http://localhost:8000/api/posts/?page=2&page_size=5",
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "john_doe",
            "title": "Django REST API Tutorial",
            "content": "Learn how to build APIs with DRF...",
            "created_at": "2026-02-21T15:30:00Z",
            "updated_at": "2026-02-21T15:30:00Z",
            "comments_count": 3
        },
        ...
    ]
}
Create Post

URL: /posts/

Method: POST

Permissions: Authenticated

Description: Create a new post. Author is automatically set to the logged-in user.

Request Body:

{
    "title": "My First Post",
    "content": "Hello world! This is my first post."
}

Response Example:

{
    "id": 13,
    "author": "jane_doe",
    "title": "My First Post",
    "content": "Hello world! This is my first post.",
    "created_at": "2026-02-21T16:00:00Z",
    "updated_at": "2026-02-21T16:00:00Z",
    "comments_count": 0
}
Retrieve / Update / Delete Post

URL: /posts/{id}/

Methods: GET, PUT, PATCH, DELETE

Permissions: Only the author can update or delete; others can read.

Update Request Example (PATCH):

{
    "title": "Updated Post Title"
}

Response Example:

{
    "id": 13,
    "author": "jane_doe",
    "title": "Updated Post Title",
    "content": "Hello world! This is my first post.",
    "created_at": "2026-02-21T16:00:00Z",
    "updated_at": "2026-02-21T16:15:00Z",
    "comments_count": 0
}
2️⃣ Comments Endpoints
List Comments

URL: /comments/

Method: GET

Description: Retrieve a paginated list of all comments.

Query Parameters:

Parameter	Type	Description
page	int	Page number
page_size	int	Number of comments per page

Example Response:

{
    "count": 8,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "post_id": 5,
            "author": "john_doe",
            "content": "Great post!",
            "created_at": "2026-02-21T16:05:00Z",
            "updated_at": "2026-02-21T16:05:00Z"
        },
        ...
    ]
}
Create Comment

URL: /comments/

Method: POST

Permissions: Authenticated

Request Body:

{
    "post_id": 13,
    "content": "Congratulations on your first post!"
}

Response Example:

{
    "id": 9,
    "post_id": 13,
    "author": "john_doe",
    "content": "Congratulations on your first post!",
    "created_at": "2026-02-21T16:20:00Z",
    "updated_at": "2026-02-21T16:20:00Z"
}
Retrieve / Update / Delete Comment

URL: /comments/{id}/

Methods: GET, PUT, PATCH, DELETE

Permissions: Only the author can edit or delete.

Example Update Request:

{
    "content": "Updated comment text."
}
3️⃣ Pagination & Searching Notes

Pagination is automatic. You can pass page and page_size query parameters.

Post search works via search query parameter:

GET /api/posts/?search=django
4️⃣ Authentication

All endpoints require token authentication (except read-only GET requests if you prefer).

Send the token in the header:

Authorization: Token <your-token>