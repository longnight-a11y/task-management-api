# Task Management API

## Overview

This is a RESTful Task Management API built with FastAPI.
It supports user authentication using JWT and allows users to manage their own tasks securely.

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy (ORM)
* Pydantic
* JWT (python-jose)
* Passlib (Argon2)

---

## Features

### Authentication

* User registration
* Login with JWT
* Token-based authentication

### Task Management

* Create tasks (authenticated users only)
* Get all tasks with pagination
* Get only your tasks
* Get a single task with user information
* Update your own tasks
* Delete your own tasks

### Security

* Password hashing using Argon2
* JWT token validation
* Authorization (only the owner can modify/delete tasks)

---

## API Endpoints

### Auth

* POST /auth/login

### Users

* POST /users
* GET /users/me

### Tasks

* POST /tasks
* GET /tasks?page=1&limit=10
* GET /tasks/me
* GET /tasks/{task_id}
* PUT /tasks/{task_id}
* DELETE /tasks/{task_id}

---

## Pagination Example

Response format:

```
{
  "items": [...],
  "total": 50,
  "page": 1,
  "size": 10
}
```

---

## How to Run

1. Clone the repository

```
git clone https://github.com/longnight-a11y/task-management-api.git
cd task-management-api
```

2. Create a `.env` file

```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the server

```
uvicorn main:app --reload
```

---

## Future Improvements

* Refresh token support
* Docker support
* Deployment (Render / Railway)
* Unit testing

---

## Author

* Mirai
