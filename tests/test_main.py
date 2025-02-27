import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import SessionLocal, Base, engine

# Create a TestClient instance
client = TestClient(app)

# Create the database tables
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def test_db():
    # Create a new database session for testing
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_register_user(test_db):
    response = client.post("/auth/register", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}

def test_login_user(test_db):
    # Register the user first
    client.post("/auth/register", json={"username": "testuser", "password": "testpassword"})
    
    # Now login with the registered user
    response = client.post("/auth/login", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"