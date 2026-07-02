from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data
from scripts.visualize import visualize_data


def main():
    print("=" * 50)
    print("🚀 Starting Data Engineering Pipeline")
    print("=" * 50)

    extract_data()
    transform_data()
    load_data()
    visualize_data()

    print("\n✅ Pipeline completed successfully!")


if __name__ == "__main__":
    main()