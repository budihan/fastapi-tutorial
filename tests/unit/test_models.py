"""Unit tests for database models."""

from app.blog.models import User, Blog


def test_user_model_creation():
    """Test that User model can be instantiated."""
    user = User(
        id=1, name="testuser", email="test@example.com", password="hashedpassword"
    )

    assert user.id == 1  # type: ignore
    assert user.name == "testuser"  # type: ignore
    assert user.email == "test@example.com"  # type: ignore


def test_blog_model_creation():
    """Test that Blog model can be instantiated."""
    blog = Blog(id=1, title="Test Post", body="Test content", user_id=1)

    assert blog.id == 1  # type: ignore
    assert blog.title == "Test Post"  # type: ignore
    assert blog.body == "Test content"  # type: ignore
    assert blog.user_id == 1  # type: ignore
