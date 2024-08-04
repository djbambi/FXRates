"""This is the test file to test the 'fetch_exchange_rates' function."""
from unittest.mock import patch

from exchange_rates.ecb_api_handler import fetch_exchange_rates

def test_fetch_exchange_rates_with_date():
    """
    Test that the fetch_exchange_rates function correctly constructs the URL
    and fetches data when provided with a specific date.
    """
    last_fetched_date = "2024-01-01T00%3A00%3A00%2B01%3A00"
    expected_url = (
    "https://data-api.ecb.europa.eu/service/data/EXR/D..EUR.SP00.A?"
    "format=csvdata&updatedAfter="
    f"{last_fetched_date}"
)
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = "Mock CSV Data"

        result = fetch_exchange_rates(last_fetched_date)

        mock_get.assert_called_once_with(expected_url)
        assert result == "Mock CSV Data"