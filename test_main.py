import pytest
from fastapi.testclient import TestClient
from main import app

# Fixture to provide a reusable test client
@pytest.fixture
def client():
    """
    creates a test client instance for the FastAPI app.
    This fixture simplifies the tests and ensures a fresh client
    """
    return TestClient(app)

@pytest.fixture
def post_sample_data():
    return {"name": "Satyam", "age":23, "course":"AI/ML", "email":"satyam@example.com"}

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Student Management API...🚀"}


def test_add_student(client, post_sample_data):
    response = client.post("/student", json = post_sample_data) # create fake post req
    assert response.status_code == 200
    assert response.json() == post_sample_data
    assert response.json()["name"] == post_sample_data["name"]
    assert response.json()["age"] == post_sample_data["age"]
    assert response.json()["email"] == post_sample_data["email"]
    assert response.json()["course"] == post_sample_data["course"]


def test_get_all_student(client):
    response = client.get("/student/all")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 
    assert len(response.json()) >= 1


def test_get_student(client, post_sample_data):
    response = client.get("/student/0")
    assert response.json() == post_sample_data
    assert len(response.json()) >= 1


def test_update_student(client, post_sample_data):
    updated_smaple_data = {**post_sample_data, "name":"Satyam Thakur"}
    response = client.put("/student/0", json = updated_smaple_data)
    assert response.json()["data"] == updated_smaple_data
    assert response.json()["message"] == "Student updated successfully"


def test_delete_student(client):
    response = client.delete("/student/0")
    assert response.status_code == 200
    assert response.json()["message"] == "Student deleted successfully"
    get_response = client.get("/student/0")
    assert get_response.status_code == 404


# def test_filter_student(client, post_sample_data):
#     response = client.post("/student", json = post_sample_data)
#     response = client.get('/filter?query=s')
#     assert response.status_code == 200
#     assert isinstance(response.json()["search_result"], list)
#     assert len(response.json()["search_result"]) > 0