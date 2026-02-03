"""Unit tests for password hashing module."""

from app.blog.hashing import Hash


def test_hash_password_creates_different_hash():
    """Test that hashing a password creates a different hash."""
    password = "testpassword123"
    hashed = Hash.hash_password(password)

    assert hashed != password
    assert len(hashed) > len(password)


def test_verify_password_with_correct_password():
    """Test that verify_password returns True for correct password."""
    password = "testpassword123"
    hashed = Hash.hash_password(password)

    assert Hash.verify_password(password, hashed) is True


def test_verify_password_with_incorrect_password():
    """Test that verify_password returns False for incorrect password."""
    password = "testpassword123"
    wrong_password = "wrongpassword"
    hashed = Hash.hash_password(password)

    assert Hash.verify_password(wrong_password, hashed) is False


def test_hash_password_is_consistent():
    """Test that the same password always produces different hashes (bcrypt uses salt)."""
    password = "testpassword123"
    hash1 = Hash.hash_password(password)
    hash2 = Hash.hash_password(password)

    # Different hashes (due to salt)
    assert hash1 != hash2
    # But both verify against the same password
    assert Hash.verify_password(password, hash1) is True
    assert Hash.verify_password(password, hash2) is True
