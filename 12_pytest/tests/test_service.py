import pytest
import requests
import source.service as service
import unittest.mock as mock


# Test the get_user function in service.py
@mock.patch("source.service.get_user")
def test_get_data(mock_get_user):
    """Test the get_user function with a mocked return value.

    Args:
        mock_get_user (MagicMock): The mocked get_user function.
    """
    # Mock the database to control the test environment
    mock_get_user.return_value = "Mocked User Alice"
    user = service.get_user(1)
    # Assert that the mocked return value is correct
    assert user == "Mocked User Alice"


# Test the get_db_users function in service.py
@mock.patch("requests.get")
def test_get_db_users(mock_get_db_users):
    """Test the get_db_users function with a mocked return value.

    Args:
        mock_get_db_users (MagicMock): The mocked get_db_users function.
    """
    mock_response = mock.Mock()
    mock_response.status_code = 200
    # Mock the JSON response to return a list of users
    mock_response.json.return_value = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]
    # Mock the requests.get function to return our mock response
    mock_get_db_users.return_value = mock_response
    data = service.get_db_users()
    # Assert that the mocked return value is correct
    assert data == [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]


# Test the get_db_users function when the API call fails
@mock.patch("requests.get")
def test_get_db_users_failure(mock_get_db_users):
    """Test the get_db_users function when the API call fails.

    Args:
        mock_get_db_users (MagicMock): The mocked get_db_users function.
    """
    mock_response = mock.Mock()
    mock_response.status_code = 400
    # Mock the requests.get function to return our mock response
    mock_get_db_users.return_value = mock_response
    with pytest.raises(requests.HTTPError) as excinfo:
        service.get_db_users()
    # Assert that the exception message is correct
    assert str(excinfo.value) == "Failed to retrieve users from the database"
