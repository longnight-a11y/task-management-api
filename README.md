# Task Management API

## Overview

This is a RESTful Task Management API built with FastAPI.
The goal of this project is to demonstrate my backend development skills including authentication, authorization, database design, and API architecture.
It simulates a real-world task management system where users can manage their own tasks securely.
This project is designed with production-level considerations such as scalability, security, and clean architecture.

---

## Live Demo

API Docs:
https://task-management-api-production-f884.up.railway.app/docs

---


## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy (ORM)
* Pydantic
* JWT (python-jose)
* Passlib (Argon2)

---

## Why These Technologies?

* FastAPI: High performance and automatic API documentation
* PostgreSQL: Reliable relational DB for structured data
* SQLAlchemy: Flexible ORM that allows us to handle DB operations within Python code
* JWT: Allows the server to verify user identity without storing session data(stateless), provides scalability  

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

### Security Design

* Passwords are hashed using Argon2
* JWT tokens are validated for each request
* Authorization ensures users can only access their own resources

### Technical Highlights

* JWT-based authentication and authorization for scalability
* Pagination with total count
* Prevention of N+1 problem using selectinload
* Clean coding with routers and dependency injection

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

## How to Use on Swagger UI

1. Create a new user via **POST /users** endpoint
2. Login via **Authorize** button (client_id and client_secret should be blank)
3. Access protected endpoints!

---

## Future Improvements

* Refresh token support
* Docker support
* Unit testing

---

## Author

* Mirai (longnight-a11y)
