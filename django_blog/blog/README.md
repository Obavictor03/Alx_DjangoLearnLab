🔐 Authentication System Documentation
📌 Overview

The authentication system manages how users:

Create accounts (Registration)

Log in (Authentication)

Log out (Session termination)

View and edit their profiles

Access protected features

Django’s built-in authentication framework is used for security, reliability, and ease of development.

🧠 Components of the Authentication System
1️⃣ User Model

The system uses Django’s built-in User model, which stores:

Username

Email

Password (securely hashed)

Permissions

Account status

Passwords are never stored as plain text.

2️⃣ Registration (Sign Up)
✔ Purpose

Allows new users to create an account.

✔ Implementation

A custom registration view uses an extended UserCreationForm to collect:

Username

Email

Password

Password confirmation

✔ Process Flow

User visits /register

Fills out registration form

Form is validated

User account is created

User is redirected to login page

✔ Interaction Example
User → Submit form → Server validates → Account created → Redirect to login

3️⃣ Login (Authentication)
✔ Purpose

Verifies user identity and starts a session.

✔ Implementation

Uses Django’s built-in LoginView.

✔ Process Flow

User visits /login

Enters username and password

Credentials checked against database

Session created if valid

User redirected to homepage or dashboard

✔ Security Features

Password hashing

Session-based authentication

CSRF protection

Brute-force protection (basic)

4️⃣ Logout
✔ Purpose

Ends the authenticated session.

✔ Implementation

Uses Django’s built-in LogoutView.

✔ Process Flow

User clicks logout

Session is destroyed

User becomes anonymous

Redirected to homepage or login page

5️⃣ Profile Management
✔ Purpose

Allows users to view and update personal information.

✔ Features

Users can update:

Email address

Bio (optional)

Profile picture (optional)

✔ Implementation

A custom view handles both:

Displaying profile data

Updating information via POST request

Only authenticated users can access this page.

6️⃣ Authorization (Access Control)

Certain features are restricted to logged-in users.

Example protected actions:

Creating posts

Editing profile

Viewing personal content

Implemented using:

@login_required decorator


Unauthenticated users are redirected to the login page.

🔄 Authentication Workflow
🔹 Registration → Login → Authenticated Session → Logout
Register → Login → Access Protected Pages → Logout

👥 User Interaction Flow
New User Journey

Visit /register

Create account

Redirect to /login

Log in

Access profile and blog features

Returning User Journey

Visit /login

Enter credentials

Access authenticated features

Logout when finished

⚙️ Session Management

Django uses session cookies to remember logged-in users.

Key characteristics:

Stored securely on server

Automatically expires

Invalidated on logout

🧪 Testing Instructions
✅ Test Registration

Navigate to:

/register


Enter valid details

Submit form

Expected Result

Account created

Redirect to login page

Test Invalid Cases

Try:

❌ Existing username
❌ Weak password
❌ Mismatched passwords

System should display error messages.

✅ Test Login

Go to:

/login


Enter valid credentials

Expected Result

Successful login

Redirect to homepage/profile

Test Invalid Cases

❌ Wrong password
❌ Nonexistent username

Should display authentication error.

✅ Test Logout

Click logout link or visit:

/logout

Expected Result

User logged out

Redirected to public page

Protected pages inaccessible

✅ Test Profile Page

Log in

Navigate to:

/profile

Expected Result

User information displayed

Editable form available

✅ Test Profile Update

Modify email or bio

Upload profile picture (if enabled)

Submit form

Expected Result

Changes saved

Updated info displayed

✅ Test Access Control
While Logged Out

Attempt to visit:

/profile


Expected:

👉 Redirect to login page

🔒 Security Considerations

The system includes:

Password hashing

CSRF protection

Session management

Access restrictions

Form validation