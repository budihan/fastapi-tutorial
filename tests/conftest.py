import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """FastAPI test client fixture."""
    return TestClient(app)


@pytest.fixture
def authenticated_client(client, test_user_data):
    """FastAPI test client with authentication token."""
    # Create a user (schemas expect `name` field)
    client.post("/user/", json=test_user_data)

    # Login to get access token (OAuth2 form uses 'username')
    response = client.post(
        "/auth/login",
        data={
            "username": test_user_data["name"],
            "password": test_user_data["password"],
        },
    )

    # Extract token from response
    token = response.json().get("access_token")
    if not token:
        # surface the error for easier debugging
        raise RuntimeError(
            f"Failed to get access token: {response.status_code} {response.text}"
        )

    # Add authorization header to client
    client.headers.update({"Authorization": f"Bearer {token}"})

    return client


@pytest.fixture
def test_user_data():
    """Sample user data for testing."""
    return {
        "name": "testuser",
        "email": "test@example.com",
        "password": "testpassword123",
    }


@pytest.fixture
def test_blog_data():
    """Sample blog post data for testing."""
    return {
        "title": "Test Blog Post",
        "body": "This is a test blog post",
        "published": True,
    }
