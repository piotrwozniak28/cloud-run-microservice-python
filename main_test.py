# import pytest
# from flask import Flask
# from your_app import app, generate_random_number, generate_random_string

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         yield client

# def test_generate_random_number():
#     # Test that the function returns a single digit string
#     result = generate_random_number()
#     assert isinstance(result, str)
#     assert len(result) == 1
#     assert result.isdigit()
#     assert 0 <= int(result) <= 9

# def test_generate_random_string():
#     # Test that the function returns a single character
#     result = generate_random_string()
#     assert isinstance(result, str)
#     assert len(result) == 1
#     assert result.isalpha()

# def test_home_endpoint(client):
#     # Test the response status code and content
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.data == b"Hello World!"
    
#     # Test response headers
#     assert 'Authorization' in response.headers
#     assert len(response.headers['Authorization']) == 1
#     assert response.headers['Authorization'].isdigit()
    
#     assert 'X-Token' in response.headers
#     assert len(response.headers['X-Token']) == 1
#     assert response.headers['X-Token'].isalpha()

# def test_home_endpoint_different_responses(client):
#     # Test that multiple requests generate different header values
#     response1 = client.get('/')
#     response2 = client.get('/')
    
#     assert response1.headers['Authorization'] != response2.headers['Authorization'] or \
#            response1.headers['X-Token'] != response2.headers['X-Token']
