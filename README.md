# ML-segmentation-project
# Indian EV Segmentation Project

This project analyzes and clusters Indian electric vehicles (EVs) based on their features such as battery capacity, range, price, and performance metrics. The goal is to identify distinct segments of EVs for better understanding and decision-making.

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Code Snippets](#code-snippets)
- [Visualizations](#visualizations)
- [Dataset Description](#dataset-description)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Shaunrufus/ML-segmentation-project.git
   cd ML-segmentation-project
install required dependencies
    pip install -r requirements.txt

Run the processing script
   python src/data_preprocessing.py

 
Run the clustering script
   python src/clustering.py

   Usage
Preprocessing
The data_preprocessing.py script cleans and preprocesses the raw dataset (indian-ev-data.csv) to handle missing values and prepare it for analysis.

Clustering
The clustering.py script performs K-Means clustering on the preprocessed data and saves the results in the data/ folder.

Analysis
The EDA.ipynb notebook contains code for analyzing and visualizing the clustered data.

Code Snippets
Data Preprocessing
Below is an example of how missing values are handled in the preprocessing step:
# Fill missing values in 'Power (kW)' column with 0
if data['Power (kW)'].isnull().all():
    data['Power (kW)'] = 0

K-Means Clustering
Here’s how K-Means clustering is performed:
 from sklearn.cluster import KMeans

# Perform K-Means clustering
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

Visualizations
Elbow Method
The Elbow Method is used to determine the optimal number of clusters:
![image](https://github.com/user-attachments/assets/3e64e232-cb23-484f-8166-d3dee7e7af0e)


Cluster Visualization
Below is a scatter plot showing the clusters based on Price and Range per Charge:
![image](https://github.com/user-attachments/assets/1a8a7630-0aad-4d13-b08c-12deb83ca8a2)[table-465363af-1425-4f31-8315-608f788486a8-45.csv](https://github.com/user-attachments/files/18607557/table-465363af-1425-4f31-8315-608f788486a8-45.csv)


Dataset Description
The dataset contains information about 50 Indian electric vehicles (EVs). Each row represents a vehicle with the following attributes:
https://1drv.ms/x/c/2c5ef1fba480cf11/EaHKnxSm4qNLnvT1C45IRHwBdu0IFhs5jZ5uGqRvL2iyTQ?e=JdkU2S

Dataset Preview
Below is a sample of the dataset:
https://1drv.ms/x/c/2c5ef1fba480cf11/EbCjlXhUuS9BtReMRSgzKr0BzPgeGOwdxUfxIbg-hBROKA?e=ZOXpxF


Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.


License
This project is licensed under the MIT License. See the LICENSE file for details.


---

### **Key Notes Before Pasting**
1. **Update File Paths**:
   - Ensure the paths to images (`reports/elbow_method.png`, `reports/clusters_price_vs_range.png`) and dataset files (`data/indian-ev-data.csv`) are correct.
   - If you’re hosting images on GitHub, use the raw image URL. For example:
     ```markdown
     ![Elbow Method Plot](https://raw.githubusercontent.com/Shaunrufus/ML-segmentation-project/main/reports/elbow_method.png)
     ```

2. **Verify Image Uploads**:
   - Make sure all images are uploaded to the `reports/` folder in your repository.

3. **Check Dataset File**:
   - Ensure the dataset file (`indian-ev-data.csv`) exists in the `data/` folder.

4. **Test Rendering**:
   - After pasting, use the **Preview** tab in GitHub to confirm that the `README.md` renders correctly.

---

### **Final Steps**
1. Paste the content into the GitHub editor.
2. Commit the changes.
3. Verify the rendered `README.md` on your repository’s main page.

Let me know if you need further assistance! 😊




