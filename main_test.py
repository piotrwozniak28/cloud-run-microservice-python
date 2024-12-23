import pytest
from main import app, generate_random_number, generate_random_string

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_generate_random_number():
    result = generate_random_number()
    assert isinstance(result, str)
    assert len(result) == 16
    assert result.isdigit()

def test_generate_random_string():
    result = generate_random_string()
    assert isinstance(result, str)
    assert len(result) == 16
    assert result.isalpha()

def test_generate_random_string_custom_length():
    result = generate_random_string(length=10)
    assert isinstance(result, str)
    assert len(result) == 10
    assert result.isalpha()

def test_home_endpoint(client):
    # Test the home endpoint response
    response = client.get('/')
    
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello World!"
    assert 'Authorization' in response.headers
    assert 'X-Token' in response.headers
    
    # Test if headers contain expected format
    assert response.headers['Authorization'].isdigit()
    assert response.headers['X-Token'].isalpha()
