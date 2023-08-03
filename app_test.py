import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
from app import app, search, scrape_website, summary

client = TestClient(app)

@patch('requests.request')
@patch('os.getenv')

def test_search(mock_getenv, mock_request):
    # Arrange
    mock_getenv.return_value = 'serper_dummy_api_key'
    mock_response = Mock()
    mock_response.text = 'Test response'
    mock_request.return_value = mock_response
    query = 'Can you define digital divide?'

    # Act
    response = search(query)

    # Assert
    mock_request.assert_called_once_with("POST", "https://google.serper.dev/search", 
      headers = {
          'X-API-KEY': 'serper_dummy_api_key',
          'Content-Type': 'application/json'
      },
      data = json.dumps({
        "q": query
      })
    )
    assert response == 'Test response'

def test_scrape_website():
    # Test the scrape_website function here
    pass

def test_summary():
    # Test the summary function here
    pass

def test_researchAgent():
    # Test the researchAgent endpoint here
    pass
