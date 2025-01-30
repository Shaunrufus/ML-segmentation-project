import pandas as pd
import numpy as np

# Load the dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        return data
    except Exception as e:
        print(f"Error loading the dataset: {e}")
        return None

# Explore the dataset
def explore_data(data):
    print("\nFirst 5 rows of the dataset:")
    print(data.head())  # Display the first 5 rows

    print("\nDataset Info:")
    print(data.info())  # Get information about columns, data types, and missing values

    print("\nSummary Statistics:")
    print(data.describe())  # Get summary statistics for numerical columns

    print("\nMissing Values:")
    print(data.isnull().sum())  # Count missing values in each column

# Preprocess the dataset
def preprocess_data(data):
    # Drop rows with missing values
    data = data.dropna()

    # Convert 'Power' column to numeric (handle HP and kW)
    def convert_power(power):
        if isinstance(power, str):
            if 'HP' in power:
                return float(power.replace('HP', '').strip()) * 0.746  # Convert HP to kW
            elif 'kW' in power:
                return float(power.replace('kW', '').strip())
        return np.nan

    data['Power (kW)'] = data['Power (HP or kW)'].apply(convert_power)

    # Drop unnecessary columns
    data = data.drop(columns=['id', 'Power (HP or kW)'], errors='ignore')

    print("\nPreprocessed Dataset:")
    print(data.head())

    return data

# Main function
if __name__ == "__main__":
    # Replace 'data/indian-ev-data.csv' with the actual path to your CSV file
    file_path = "data/indian-ev-data.csv"
    data = load_data(file_path)
    if data is not None:
        explore_data(data)
        preprocessed_data = preprocess_data(data)
        # Save the preprocessed data to a new CSV file
        preprocessed_data.to_csv("data/preprocessed_indian_ev_data.csv", index=False)
        print("\nPreprocessed data saved to 'data/preprocessed_indian_ev_data.csv'")
        file_path = "C:/ML-project3-indian-ev/data/indian-ev-data.csv"