# tests/test_app.py
# Tests for FastAPI app using Arrange-Act-Assert (AAA) pattern

def test_get_activities(client):
    # Arrange: client fixture provided
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_valid(client):
    # Arrange
    email = "newuser@mergington.edu"
    activity = "Basketball Club"
    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert response.status_code == 200
    assert "message" in response.json()

def test_signup_invalid_activity(client):
    # Arrange
    email = "test@mergington.edu"
    activity = "Nonexistent"
    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert response.status_code == 404
    assert "detail" in response.json()
