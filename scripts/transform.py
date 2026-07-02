import json
import pandas as pd


def transform_data():
    # Read raw JSON data
    with open("data/raw_data.json", "r") as file:
        data = json.load(file)

    # Select required fields
    transformed_data = {
        "Country": data["country"],
        "Cases": data["cases"],
        "Recovered": data["recovered"],
        "Deaths": data["deaths"],
        "Active": data["active"],
        "Tests": data["tests"],
        "Population": data["population"]
    }

    # Convert to DataFrame
    df = pd.DataFrame([transformed_data])

    # Save as CSV
    df.to_csv("data/cleaned_data.csv", index=False)

    print("✅ Data transformed successfully!")
    print(df)

    return df


if __name__ == "__main__":
    transform_data()