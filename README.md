# TextClustering-TFIDF-KMeans
📊 A Python pipeline for clustering text data from CSV files using TF-IDF vectorization and K-Means clustering.
## Description  
This repository contains a Python script that processes CSV data to group similar text entries using NLP and machine learning techniques. Designed for organizing search results, content analysis, or document categorization.  

```python
# Key Features
- CSV data preprocessing (handles missing values)
- Text combination (Title + Description)
- TF-IDF vectorization for feature extraction
- K-Means clustering implementation
- Automated output sorting and CSV export
```

---

## README.md

# 📂 TextClustering-TFIDF-KMeans

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-pandas%20|%20scikit--learn-orange)

A lightweight text clustering pipeline for organizing unstructured CSV data.

## 🚀 Overview
This script processes CSV files containing text columns (e.g., search results, product descriptions) and groups similar entries using:
1. **TF-IDF Vectorization** to convert text to numerical features
2. **K-Means Clustering** to identify semantic patterns

## 🛠️ Installation
```bash
git clone https://github.com/Yonatankinfe/TextClustering-TFIDF-KMeans.git
cd TextClustering-TFIDF-KMeans
pip install -r requirements.txt
```

## 📋 Usage
1. Place your CSV file in the project directory
2. Modify `file_path` variable in `clustering_pipeline.py`:
```python
file_path = "your_data.csv"  # Replace with your CSV path
num_clusters = 5  # Adjust based on desired grouping granularity
```
3. Run the script:
```bash
python clustering_pipeline.py
```

## 📂 Output
- Generates `clustered_output.csv` with new `cluster` column
- Rows sorted by cluster ID for easy analysis

## 🔧 Dependencies
- pandas
- scikit-learn
- numpy

## 🤖 Customization Tips
- Modify `num_clusters` for different grouping densities
- Add text preprocessing (stemming, lemmatization) in the `combined` column step
- Experiment with other clustering algorithms (DBSCAN, Hierarchical)

## 🤝 Contributing
Pull requests welcome! For major changes, please open an issue first.

## 📜 License
MIT License - see [LICENSE](LICENSE) for details
```
