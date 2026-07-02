import requests
import json
import os


def extract_data():
    url = "https://disease.sh/v3/covid-19/countries/India"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        os.makedirs("data", exist_ok=True)

        with open("data/raw_data.json", "w") as file:
            json.dump(data, file, indent=4)

        print("✅ Data extracted successfully!")
        return data

    else:
        print("❌ Failed to fetch data.")
        return None


if __name__ == "__main__":
    extract_data()