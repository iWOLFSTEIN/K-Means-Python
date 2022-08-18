import csv
import random

dataset = []

def analyzer(age):
    if age <= 30 and age >=11:
        return [10000, 39999]
    elif age <= 50 and age >=31:
        return [80000, 100000]
    elif age <= 70 and age >=51:
        return [40000, 79999]

for i in range(200):  
    j = random.randint(11, 70)
    k = analyzer(j)   
    l = random.randint(k[0], k[1])
    dataset.append([j,l])

with open('E:\Visual Code Projects\Python Projects\python\Machine Learning\datasets\k_means_dataset2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Age", "Income"])
    writer.writerows(dataset)

    


