# DISCLAIMER:
# This sample code is provided for illustrative purposes only.
# It is not intended for production use and comes with no warranties.

import argparse
import requests

from models import RootModel

def fetch_feed_last_datum_change_on(feed_id: str, api_key: str):
    # this isn't throttled
    url = f"https://api.balticexchange.com/api/v1.3/feed/{feed_id}/latestDatumChangeOn"
    headers = {
        "x-apikey": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError if status code is 4xx or 5xx

        data = response.json()
        print("Datum Change On: Response JSON:")
        print(data)
        return data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print("Response content:", response.text)
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print("Error parsing JSON:", json_err)
        print("Raw response content:", response.text)

def fetch_feed_data(feed_id: str, api_key: str):
    # this IS throttled
    url = f"https://api.balticexchange.com/api/v1.3/feed/{feed_id}/data"
    headers = {
        "x-apikey": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError if status code is 4xx or 5xx

        data = response.json()
        print("Data: Response JSON:")
        parsed = RootModel.model_validate(data)
        print(parsed)
        return data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print("Response content:", response.text)
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print("Error parsing JSON:", json_err)
        print("Raw response content:", response.text)

# Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demo script for command line arguments")
    parser.add_argument("--feedid", type=str, help="Your Feed ID")
    parser.add_argument("--apikey", type=str, help="Your API Key")

    args = parser.parse_args()

    feed_id = args.feedid or input("Input your Feed ID: ")
    api_key = args.apikey or input("Input your API Key: ")

    fetch_feed_last_datum_change_on(feed_id, api_key)
    fetch_feed_data(feed_id, api_key)
