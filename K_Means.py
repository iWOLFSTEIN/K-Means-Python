import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import csv

df = pd.read_csv('E:\Visual Code Projects\Python Projects\python\Machine Learning\KMeans\k_means_dataset.csv')
new_df = df.copy()

scaler = MinMaxScaler()
scaler.fit(df[["Age"]])
df['Age'] = scaler.transform(df[["Age"]])
scaler.fit(df[["Income"]])
df['Income'] = scaler.transform(df[["Income"]])

km = KMeans(n_clusters=3)
predicted_array =km.fit_predict(df[["Age", "Income"]])

new_df['clusters'] = predicted_array
with open('E:\Visual Code Projects\Python Projects\python\Machine Learning\KMeans\\k_means_dataset_clustered.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Age", "Income", "Clusters"])
    writer.writerows(new_df.values)