"""
Integration tests for Flask API endpoints
Tests REST API functionality and error handling.
"""
import pytest
from app import create_app


@pytest.fixture
def client():
    """Create test client."""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHealthEndpoint:
    """Test health check endpoint."""

    def test_health_check(self, client):
        response = client.get('/api/health')
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert 'service' in data
        assert 'version' in data


class TestBasicOperationsAPI:
    """Test basic arithmetic operations via API."""

    def test_addition(self, client):
        response = client.post('/api/calculate',
                                json={'operation': '+', 'num1': 5, 'num2': 3})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert data['result'] == 8

    def test_subtraction(self, client):
        response = client.post('/api/calculate',
                                json={'operation': '-', 'num1': 10, 'num2': 3})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert data['result'] == 7

    def test_multiplication(self, client):
        response = client.post('/api/calculate',
                                json={'operation': '*', 'num1': 5, 'num2': 4})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert data['result'] == 20

    def test_division(self, client):
        response = client.post('/api/calculate',
                                json={'operation': '/', 'num1': 10, 'num2': 2})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert data['result'] == 5

    def test_division_by_zero(self, client):
        response = client.post('/api/calculate',
                                json={'operation': '/', 'num1': 10, 'num2': 0})
        assert response.status_code == 400
        data = response.get_json()
        assert data['success'] is False
        assert 'error' in data


class TestScientificOperationsAPI:
    """Test scientific operations via API."""

    def test_sin(self, client):
        response = client.post('/api/calculate',
                                json={'operation': 'sin', 'angle': 30})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert abs(data['result'] - 0.5) < 1e-10

    def test_cos(self, client):
        response = client.post('/api/calculate',
                                json={'operation': 'cos', 'angle': 60})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert abs(data['result'] - 0.5) < 1e-10

    def test_tan(self, client):
        response = client.post('/api/calculate',
                                json={'operation': 'tan', 'angle': 45})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert abs(data['result'] - 1) < 1e-10

    def test_logarithm(self, client):
        response = client.post('/api/calculate',
                                json={'operation': 'log', 'number': 100, 'base': 10})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert abs(data['result'] - 2) < 1e-10

    def test_power(self, client):
        response = client.post('/api/calculate',
                                json={'operation': 'power', 'base': 2, 'exponent': 8})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert data['result'] == 256

    def test_modulo(self, client):
        response = client.post('/api/calculate',
                                json={'operation': 'mod', 'num1': 10, 'num2': 3})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert data['result'] == 1

    def test_pi(self, client):
        response = client.post('/api/calculate',
                                json={'operation': 'pi'})
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert abs(data['result'] - 3.14159265358979) < 1e-10


class TestErrorHandling:
    """Test API error handling."""

    def test_no_data(self, client):
        response = client.post('/api/calculate')
        assert response.status_code == 400
        data = response.get_json()
        assert data['success'] is False
        assert 'error' in data

    def test_no_operation(self, client):
        response = client.post('/api/calculate',
                                json={'num1': 5, 'num2': 3})
        assert response.status_code == 400
        data = response.get_json()
        assert data['success'] is False
        assert 'error' in data

    def test_invalid_operation(self, client):
        response = client.post('/api/calculate',
                                json={'operation': 'invalid', 'num1': 5, 'num2': 3})
        assert response.status_code == 400
        data = response.get_json()
        assert data['success'] is False
        assert 'error' in data

    def test_invalid_input_type(self, client):
        response = client.post('/api/calculate',
                                json={'operation': '+', 'num1': 'abc', 'num2': 3})
        assert response.status_code == 400
        data = response.get_json()
        assert data['success'] is False
        assert 'error' in data


class TestIndexRoute:
    """Test index route."""

    def test_index_returns_html(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert b'<!DOCTYPE html>' in response.data
        assert b'Scientific Calculator' in response.data
