# User Authentication Service

This project is a **User Authentication Service** that provides secure and scalable user authentication functionalities. It includes support for basic and session-based authentication methods, ensuring that sensitive user data is securely handled. The project is built using Python, Flask, and SQLAlchemy and can be used as a base for applications that require user login, registration, and session management.

## Features

- **User Registration**: Allows users to create an account with username and password.
- **User Login**: Authenticates users with basic or session-based authentication.
- **Session Management**: Manages user sessions, allowing users to remain logged in for multiple requests.
- **Password Encryption**: Utilizes hashing algorithms to store passwords securely.
- **Token-Based Authentication (Optional)**: Supports JWT-based authentication for APIs.
- **User Role Management**: Role-based access control (optional feature).

## Technologies Used

- **Python**: Core language used for developing the service.
- **Flask**: Web framework for routing and handling requests.
- **SQLAlchemy**: ORM (Object Relational Mapping) library for interacting with the database.
- **Flask-Login**: Used for session management and user authentication.
- **Bcrypt**: For password hashing and encryption.
- **PostgreSQL**: As the database (can be swapped for other DBMS).
- **Docker**: For containerization and easy deployment (optional).
- **JWT (JSON Web Token)**: Optional for token-based authentication.

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL (or another supported database)
- Pipenv or virtualenv for environment management
- Docker (optional for containerization)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/vincenttwizere/user_authentication_service.git
   cd user_authentication_service
