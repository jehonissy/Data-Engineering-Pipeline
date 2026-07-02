import pandas as pd
import matplotlib.pyplot as plt


def visualize_data():
    # Read cleaned CSV
    df = pd.read_csv("data/cleaned_data.csv")

    # Data for chart
    labels = ["Cases", "Recovered", "Deaths", "Active"]
    values = [
        df.loc[0, "Cases"],
        df.loc[0, "Recovered"],
        df.loc[0, "Deaths"],
        df.loc[0, "Active"]
    ]

    # Create bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)

    plt.title("COVID-19 Statistics - India")
    plt.xlabel("Category")
    plt.ylabel("Count")

    plt.tight_layout()
    
    import os
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/chart.png")
    
    plt.show()

    print("✅ Visualization displayed successfully!")


if __name__ == "__main__":
    visualize_data()