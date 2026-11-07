# 🚀 CodePilot – Assessment and Evaluation Management System

A backend-focused Assessment and Evaluation Management System built using **Python, Django, Django REST Framework, and MySQL**.

CodePilot provides an API-based platform for managing students, assessments, questions, submissions, and evaluation processes with separate Admin and Student roles.

## 📌 About the Project

CodePilot is designed to simplify the assessment and evaluation process through a structured backend system.

The application supports custom user authentication, assessment creation, question management, student submissions, and answer evaluation.

This project demonstrates practical experience in REST API development, Django ORM, custom authentication, permissions, serializers, database relationships, Django signals, and automated evaluation workflows.

## ✨ Features

- **Custom User Model:** User management using Django's `AbstractUser`.
- **Multiple Authentication Methods:** Username, email, and phone number authentication.
- **Role-Based Access:** Separate Admin and Student roles.
- **Token Authentication:** Token-based authentication for Admin users.
- **JWT Authentication:** JWT-based authentication for Student users.
- **Automatic Student Profile Creation:** Django Signals create student profiles automatically.
- **Email Notifications:** Automated email notifications using Django Signals.
- **Assessment Management:** Create and manage assessments.
- **Question Management:** Manage assessment questions.
- **Student Submissions:** Handle student answers and submissions.
- **Answer Validation:** Apply submission rules and answer validation.
- **Answer Evaluation:** Admins can evaluate answers and provide marks and feedback.
- **Custom Permissions:** Control access based on user roles and ownership.
- **Automatic Model Logic:** Custom `save()` methods handle automatic end-time and numbering logic.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| Django REST Framework | REST API development |
| MySQL | Database management |
| Django ORM | Database operations |
| DRF Token Authentication | Admin authentication |
| Simple JWT | Student authentication |
| Django CORS Headers | Cross-Origin Resource Sharing |
| Django Signals | Automated profile creation and email notifications |
| Git | Version control |
| GitHub | Source code management |

## 📂 Project Structure

```text
CodePilot/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── exams/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── problem/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── evaluation/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── manage.py
└── requirements.txt
```

*Note: Adjust the folder and file names to match your actual repository structure.*

## ⚙️ Installation and Setup

### Prerequisites

Make sure the following tools and technologies are installed:

- Python
- pip
- Django
- Django REST Framework
- MySQL
- Django REST Framework Simple JWT
- Django CORS Headers
- Git
- GitHub

### 1. Clone the Repository

```bash
git clone https://github.com/thefarsin12-afk/Code_pilot.git
cd Code_pilot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate on Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure MySQL Database

Configure your MySQL database credentials in Django's `settings.py` file.

Make sure the database exists and the configured database user has the required permissions.

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

The local development server will normally run at:

```text
http://127.0.0.1:8000/
```

## 🔐 Authentication

CodePilot implements a custom authentication system using Django's `AbstractUser` model and custom authentication backends.

### Authentication Methods

- Username authentication
- Email authentication
- Phone number authentication

### Admin Authentication

Admin users authenticate using Django REST Framework Token Authentication.

### Student Authentication

Student users authenticate using JSON Web Token (JWT) Authentication through Simple JWT.

Protected API requests must include the appropriate authentication credentials.

## 👥 User Roles

### Admin

- Manage assessments.
- Create and manage questions.
- Access student submissions.
- Evaluate submitted answers.
- Update marks and feedback.

### Student

- Access available assessments.
- View assessment questions.
- Submit answers.
- Access relevant profile and evaluation information.

## 🔌 API Endpoints

CodePilot provides REST API endpoints for account management, assessments, questions, and evaluation.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/account/me/` | Retrieve authenticated user details |
| GET | `/account/profile/complted/` | Retrieve completed profile information |
| GET | `/problem/assesment/<id>/question/` | Access questions for an assessment |
| GET | `/problem/question/<id>/` | Retrieve an individual question |
| `/evalution/...` | Evaluation APIs | Answer evaluation and related operations |

*Note: Endpoint spellings are retained as provided in the project details. Add the remaining methods and exact evaluation routes from your Django URL configuration.*

## ⚙️ Technical Implementation

### Custom User Model

- Uses Django's `AbstractUser`.
- Supports multiple authentication identifiers.
- Implements custom authentication backends.

### Django Signals

- Automatically creates student profiles.
- Handles email notifications.

### Assessment and Question Management

- Assessment creation and management.
- Question creation and management.
- Assessment-question relationships.

### Submission and Evaluation

- Student answer submission.
- Submission validation rules.
- Admin-side answer evaluation.
- PATCH-based grading updates.
- Marks and feedback management.

### Custom Model Logic

- Automatic end-time handling through model `save()` logic.
- Automatic numbering logic.
- Custom validation and business rules.

### Permissions

- Custom `IsOwner` permission.
- Role-based access restrictions.
- Protected API operations.

## 🧪 Testing

Recommended API test cases:

- User registration and authentication.
- Username, email, and phone number authentication.
- Admin and Student access permissions.
- Automatic student profile creation.
- Assessment creation and management.
- Question creation and retrieval.
- Student answer submission.
- Submission validation.
- Admin answer grading.
- Marks and feedback updates.
- Unauthorized access and invalid request handling.

## 🔒 Security

- Custom authentication backends.
- Token Authentication for Admin users.
- JWT Authentication for Student users.
- Role-based permissions.
- Owner-based access control.
- Input validation through serializers.
- Protected API endpoints.

## 🚀 Future Improvements

- Add automated API testing.
- Improve API documentation using OpenAPI/Swagger.
- Enhance error handling and response consistency.
- Add advanced assessment filtering.
- Improve reporting and evaluation summaries.
- Add production-ready deployment configuration.

## 👨‍💻 Author

**Muhammad Farsin M**

GitHub: [@Muhammed_Farsin_M](https://github.com/thefarsin12-afk)

Project Repository: [CodePilot](https://github.com/thefarsin12-afk/Code_pilot)

---

**CodePilot – Assessment and Evaluation Management System**

*Building, Learning, and Improving through Backend Development.*
