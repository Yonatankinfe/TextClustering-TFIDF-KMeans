import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Step 1: Load the CSV file
file_path = "/content/google_results_alex_pereira.csv"
df = pd.read_csv(file_path)

# Step 2: Handle missing values and combine Title and Description
df['Title'] = df['Title'].fillna("")  # Replace NaN in Title with an empty string
df['Description'] = df['Description'].fillna("")  # Replace NaN in Description with an empty string
df['combined'] = df['Title'] + " " + df['Description']

# Step 3: Vectorize the text using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['combined'])

# Step 4: Use KMeans for clustering
num_clusters = 5  # You can adjust this number based on your dataset
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Step 5: Group by cluster and save the results
df = df.sort_values(by='cluster')
output_file_path = '/content/edited.csv'
df.to_csv(output_file_path, index=False)

print(f"The data has been grouped and saved to {output_file_path}")
