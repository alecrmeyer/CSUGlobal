import pandas as pd
import numpy as np
import csv
import os

dirname = os.path.dirname(__file__)
datafilename = os.path.join(dirname, 'data.csv')


def pandas_knn(datafilename, y, k):
    data = pd.read_csv(datafilename)
    df = pd.DataFrame(data)
    train_X = df.loc[:, df.columns != 'game_cat']
    train_y = df['game_cat']

    def euclidean_distance(row):
        distance = 0.0
        for i in range(len(row)-1):
            distance += (row.iloc[i] - y[i])**2
        return np.sqrt(distance)
    
    k = 5
    train_X['dist'] = train_X.apply(euclidean_distance, axis=1)
    smallest = train_X.nsmallest(k, 'dist')
    vals = train_y.loc[smallest.index]
    return vals.mode()[0]

def manual_knn(datafilename, y, k):

    # 1. Load the data
    with open(datafilename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        data = list(csv.reader(csvfile))

    # 3. For getting the predicted class, iterate from 1 to total number of training data points
    for sample in data:

        # 4. Calculate the distance between test data and each row of training data
        distance = 0.0
        for i in range(len(sample)-1):
            distance += (int(sample[i])- y[i])**2
        distance = np.sqrt(distance)
        sample.append(distance)

    # 5. Sort the calculated distances in ascending order based on distance values
    data.sort(key=lambda x: x[-1])

    # 6. Get top k rows from the sorted array
    options = data[1:k]

    knn_dict = {}
    mode = ''
    max = 0
    for sample in options:
        cat = sample[-2]
        if cat in knn_dict:
            knn_dict[cat] += 1
        else:
            knn_dict[cat] = 1

        # 7. Get the most frequent class of these rows
        if knn_dict[cat] > max:
            max = knn_dict[cat]
            mode = cat

    # 8. Return the predicted class
    return mode

# 2. Initialise the value of k
k = 5
age = float(input("Enter Age: "))
height = float(input("Enter Height: "))
weight = float(input("Enter Weight: "))
gender = bool(input("Enter Gender (0 = Female, 1 = Male): "))
target = [age,height,weight,gender]

prediction_pandas = pandas_knn(datafilename, target, k)
manual_prediction = manual_knn(datafilename, target, k)
print("Prediction using Pandas DataFrame functions: " + str(prediction_pandas))
print("Prediction using manual KNN algorithm: " + str(manual_prediction))