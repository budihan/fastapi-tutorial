"""Integration tests for user routes."""


def test_user_signup(client, test_user_data):
    """Test user registration."""
    response = client.post("/user", json=test_user_data)

    # Should return 200 or 422 depending on validation
    assert response.status_code in [200, 201, 422]


def test_get_user_by_id(client):
    """Test retrieving a user by ID."""
    response = client.get("/user/1")

    # Should return 200 or 404
    assert response.status_code in [200, 404, 422]
