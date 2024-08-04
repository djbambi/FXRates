"""This handler is responsible for fetching the daily exchange rates from the ECB site."""
import requests
import logger
import platform


log = logger.get_logger(f'{platform.node()}')

def fetch_exchange_rates(last_fetched_date):

    expected_url = (
    "https://data-api.ecb.europa.eu/service/data/EXR/D..EUR.SP00.A?"
    "format=csvdata&updatedAfter="
    f"{last_fetched_date}"
)
    log.info("Sending get request to ECB api.")
    response = requests.get(expected_url)

    return response.text

fetch_exchange_rates("2024-01-01T00%3A00%3A00%2B01%3A00")