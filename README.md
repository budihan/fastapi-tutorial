# FastAPI Blog

[![codecov](https://codecov.io/github/budihan/fastapi-tutorial/graph/badge.svg?token=OfT9OhWMPS)](https://codecov.io/github/budihan/fastapi-tutorial)

A modern FastAPI blog application demonstrating best practices for building production-ready APIs with authentication, database modeling, and comprehensive testing.

## 🚀 Features

### FastAPI Routing
- **Modular routers** for blog posts, users, and authentication
- **RESTful endpoints** with proper HTTP status codes
- **Request/response validation** using Pydantic schemas
- **Dependency injection** for database sessions and authentication

### Security & Authentication
- **Password hashing** using bcrypt for secure credential storage
- **JWT tokens** for stateless authentication (python-jose)
- **OAuth2 with password flow** for user login
- **Protected endpoints** requiring valid authentication tokens

### Database & ORM
- **SQLAlchemy ORM** for database abstraction
- **SQLite** for development and testing
- **Relationship modeling** (users ↔ blog posts)
- **Automatic table creation** on startup
- **Transaction-based testing** with automatic rollback

### Data Validation
- **Pydantic schemas** for request/response validation
- **Type hints** throughout the codebase
- **Pyright type checking** in CI/CD pipeline

## 🛠️ Technology Stack

- **FastAPI** - Modern async web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type hints
- **bcrypt** - Password hashing library
- **python-jose** - JWT token handling
- **pytest** - Testing framework with parallel execution
- **Pyright** - Static type checker
- **Ruff** - Fast Python linter and formatter
- **uv** - Lightning-fast Python package installer

## 🔐 Authentication Flow

1. **User Registration** → POST `/user/`
   - Password is hashed with bcrypt
   - User stored in database

2. **User Login** → POST `/auth/login`
   - Credentials validated
   - JWT token generated (valid for 24 hours)
   - Token returned to client

3. **Protected Requests** → GET `/blog/`
   - Client sends `Authorization: Bearer {token}`
   - Token validated via OAuth2 dependency
   - Request proceeds if valid

## 📝 Database Models

### User
```python
class User(Base):
    id: int (primary key)
    name: str
    email: str
    password: str (hashed)
    blogs: list[Blog] (relationship)
```

### Blog
```python
class Blog(Base):
    id: int (primary key)
    title: str
    body: str
    user_id: int (foreign key)
    creator: User (relationship)
```

## 🧪 Testing

The project includes comprehensive tests with:

- **Unit tests** for hashing, models, and utilities
- **Integration tests** for API endpoints
- **Fixtures** for authenticated clients and test data
- **Transaction-based isolation** with automatic rollback
- **Parallel execution** with pytest-xdist
- **Coverage reporting** with pytest-cov

## 🔄 CI/CD Pipeline

GitHub Actions automatically runs on every push/PR:

- ✅ **Lock file validation** - Ensures dependencies are locked
- ✅ **Linting** - Code style checks with ruff
- ✅ **Formatting** - Code formatting validation
- ✅ **Type checking** - Static type analysis with pyright
- ✅ **Tests** - Full test suite with coverage

## 🎯 Best Practices Demonstrated

- ✅ Modular project structure
- ✅ Comprehensive type hints with pyright
- ✅ Secure password hashing with bcrypt
- ✅ JWT-based authentication
- ✅ Database transaction isolation in tests
- ✅ Pydantic schema validation
- ✅ CI/CD automation with GitHub Actions
- ✅ Fast dependency management with uv
- ✅ Parallel test execution
- ✅ Code coverage tracking