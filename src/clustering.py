import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import os

# Define the file path (absolute path)
file_path = "C:/ML-project3-indian-ev/data/preprocessed_indian_ev_data.csv"

# Print the file path for debugging
print("Attempting to load file from:", file_path)

# Load the dataset
try:
    data = pd.read_csv(file_path)
    print("File loaded successfully!")
    print("First few rows of the dataset:")
    print(data.head())
except Exception as e:
    print("Error loading the file:", e)
    exit()

# Check for missing values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())

# Handle columns with all missing values
if 'Power (kW)' in data.columns and data['Power (kW)'].isnull().all():
    print("\nColumn 'Power (kW)' has all missing values. Filling with 0.")
    data['Power (kW)'] = 0  # Fill with a default value (e.g., 0)

# Separate numeric and non-numeric columns
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
non_numeric_columns = data.select_dtypes(exclude=['float64', 'int64']).columns

# Impute missing values in numeric columns
imputer = SimpleImputer(strategy='mean')
print("Starting imputation...")
data[numeric_columns] = imputer.fit_transform(data[numeric_columns])
print("Imputation completed.")

# Combine numeric and non-numeric columns back into a single DataFrame
print("Combining numeric and non-numeric columns...")
data_imputed = pd.concat([data[non_numeric_columns], data[numeric_columns]], axis=1)
print("Combination completed.")

# Select features for clustering (only numeric columns)
features = ['Battery Capacity (kWh)', 'Range per Charge (km)', 'Price', 'Power (kW)', 'Top Speed (km/h)']
X = data_imputed[features]

# Scale the features
print("Scaling features...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("Feature scaling completed.")

# Determine the optimal number of clusters using the Elbow Method
print("Calculating inertia for the Elbow Method...")
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
    print(f"Completed iteration for k={k}")
print("Elbow Method calculation completed.")

# Plot the Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")

# Ensure the reports directory exists
os.makedirs("../reports", exist_ok=True)

# Save the Elbow Curve
plt.savefig("../reports/elbow_method.png")  # Save the plot
plt.show()

# Perform K-Means clustering with the optimal number of clusters
print("Performing K-Means clustering...")
optimal_k = 3  # Based on the Elbow Curve
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)
print("Clustering completed.")

# Save the clustered data
os.makedirs("../data", exist_ok=True)  # Ensure the data directory exists
data.to_csv("../data/clustered_indian_ev_data.csv", index=False)
print("Clustered data saved to '../data/clustered_indian_ev_data.csv'")
# Save the Elbow Curve
plt.savefig("../reports/elbow_method.png")  # Save the plot
plt.show()  # Display the plot
plt.close()  # Close the plot to avoid hanging