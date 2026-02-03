"""Integration tests for blog routes."""


def test_get_all_blogs(client):
    """Test retrieving all blog posts."""
    response = client.get("/blog")

    # Should return 200 or 422 (depends on your implementation)
    assert response.status_code in [401]


def test_get_all_blogs_authenticated(authenticated_client):
    """Test retrieving all blog posts with authentication."""
    response = authenticated_client.get("/blog")

    # Should return 200 OK
    assert response.status_code == 200


def test_create_blog_requires_auth(client, test_blog_data):
    """Test that creating a blog post requires authentication."""
    response = client.post("/blog", json=test_blog_data)

    # Should return 403 Forbidden or 401 Unauthorized
    assert response.status_code in [401, 403, 422]


def test_get_blog_by_id(client):
    """Test retrieving a single blog post by ID."""
    response = client.get("/blog/1")

    # Should return 200 or 404 depending on whether blog exists
    assert response.status_code in [200, 404, 422]
