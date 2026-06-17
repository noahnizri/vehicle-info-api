import requests
from pprint import pprint

BASE_URL = "http://localhost:8000"


def test_health():
    response = requests.get(f"{BASE_URL}/health")

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")


def test_license_plate():
    response = requests.post(
        f"{BASE_URL}/vehicle-info",
        json={
            "license_plate": "11111111",
        }
    )
    print(f"Status Code: {response.status_code}")
    pprint(response.json())



def test_invalid_license_plate():
    response = requests.post(
        f"{BASE_URL}/vehicle-info",
        json={
            "license_plate": "abc"
        }
    )

    print(f"Status Code: {response.status_code}")
    pprint(response.json())


if __name__ == "__main__":
    # test_health()
    test_license_plate()
    # test_invalid_license_plate()