import requests
from pprint import pprint

BASE_URL = "https://vehicle-info-api-6jey.onrender.com"
# for local testing:
# BASE_URL = "http://localhost:8000"


def test_health():
    response = requests.get(f"{BASE_URL}/health")

    print("\n=== HEALTH CHECK ===")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")


def test_license_plate():
    response = requests.post(
        f"{BASE_URL}/vehicle-info",
        json={
            "license_plate": "11111111",
        }
    )

    print("\n=== VALID LICENSE PLATE ===")
    print(f"Status Code: {response.status_code}")

    data = response.json()
    pprint(data)


def test_invalid_license_plate():
    response = requests.post(
        f"{BASE_URL}/vehicle-info",
        json={
            "license_plate": "abc"
        }
    )

    print("\n=== INVALID LICENSE PLATE (400) ===")
    print(f"Status Code: {response.status_code}")

    data = response.json()
    pprint(data)


def test_vehicle_not_found():
    response = requests.post(
        f"{BASE_URL}/vehicle-info",
        json={
            "license_plate": "12345678"
        }
    )

    print("\n=== VEHICLE NOT FOUND (404) ===")
    print(f"Status Code: {response.status_code}")

    data = response.json()
    pprint(data)


if __name__ == "__main__":
    test_health()
    test_license_plate()
    test_invalid_license_plate()
    test_vehicle_not_found()