"""This handler is responsible for fetching the daily exchange rates from the ECB site."""
import requests


def fetch_exchange_rates(last_fetched_date):

    expected_url = (
    "https://data-api.ecb.europa.eu/service/data/EXR/D..EUR.SP00.A?"
    "format=csvdata&updatedAfter="
    f"{last_fetched_date}"
)
    response = requests.get(expected_url)

    return response.text

