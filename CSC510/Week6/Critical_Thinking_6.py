"""
Requirements
1. Calculate the posterior probability by converting the dataset into a frequency table.
2. Create a "Likelihood" table by finding relevant probabilities.
3. Calculate the posterior probability for each class.
4. Correct Zero Probability errors using Laplacian correction.

References:
https://www.datacamp.com/tutorial/naive-bayes-scikit-learn
https://www.ibm.com/think/topics/naive-bayes
https://scikit-learn.org/stable/api/sklearn.naive_bayes.html
https://www.saedsayad.com/naive_bayesian.htm
Data - https://www.kaggle.com/datasets/fredericobreno/play-tennis
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import pandas as pd
from sklearn.metrics import accuracy_score
from io import StringIO

raw_data = StringIO("""
outlook,temp,humidity,windy,play
sunny,hot,high,false,no
sunny,hot,high,true,no
overcast,hot,high,false,yes
rainy,mild,high,false,yes
rainy,cool,normal,false,yes
rainy,cool,normal,true,no
overcast,cool,normal,true,yes
sunny,mild,high,false,no
sunny,cool,normal,false,yes
rainy,mild,normal,false,yes
sunny,mild,normal,true,yes
overcast,mild,high,true,yes
overcast,hot,normal,false,yes
rainy,mild,high,true,no
""")

# Using categorical data because continuous and binary data do not result in useful likelihood and frequency tables
# Outlook, Tempurature, Humidity, Windy, Play
data = pd.read_csv(raw_data)
df = pd.DataFrame(data)

X = df.iloc[:, 0:-1]
y = df.iloc[:, -1]

def create_likelihood_table(feature, target):
    
    # 1. Calculate the posterior probability by converting the dataset into a frequency table.
    freq_table = pd.crosstab(feature, target)
    
    # 2. Create a "Likelihood" table by finding relevant probabilities.
    likelihood_df = freq_table/freq_table.sum() 
    return likelihood_df.round(2), freq_table.round(2)  

outlook_likelihood_table, outlook_freq_table = create_likelihood_table(X['outlook'], y)
temp_likelihood_table, temp_freq_table = create_likelihood_table(X['temp'], y)
humidity_likelihood_table, humidity_freq_table = create_likelihood_table(X['humidity'], y)
windy_likelihood_table, windy_freq_table = create_likelihood_table(X['windy'], y)

# Need to encode to binary to utilize a Bernoulli classifier
# Ideally, CategoricalNB would be used here since it is categorical data, but it was not an option for this assignment
encoded_bool_data = pd.get_dummies(df)
X = encoded_bool_data.iloc[:, 0:-1]
y = encoded_bool_data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)

#4. Correct Zero Probability errors using Laplacian correction.
model = BernoulliNB(alpha=1.0) # alpha is the laplace smoothing paremeter, by default it is true
model.fit(X_train, y_train)

# 3. Calculate the posterior probability for each class.
probabilities = model.predict_proba(X_test)
y_hat = model.predict(X_test)

# Evaluate probabilities
accuracy = accuracy_score(y_test, y_hat)


#========Matplot Diplays========#
fig, axs = plt.subplots(nrows = 5, ncols = 2)

# Display Likelihood Tables
axs[0][1].axis('off')
axs[0][1].set_title("Outlook Likelihood Table")
axs[0][1].table(cellText=outlook_likelihood_table.values, colLabels=outlook_likelihood_table.columns, rowLabels = outlook_likelihood_table.index, loc='center')
axs[1][1].axis('off')
axs[1][1].set_title('Tempurature Likelihood Table')
axs[1][1].table(cellText=temp_likelihood_table.values, colLabels=temp_likelihood_table.columns, rowLabels = temp_likelihood_table.index, loc='center')
axs[2][1].axis('off')
axs[2][1].set_title('Humidity Likelihood Table')
axs[2][1].table(cellText=humidity_likelihood_table.values, colLabels=humidity_likelihood_table.columns, rowLabels = humidity_likelihood_table.index, loc='center')
axs[3][1].axis('off')
axs[3][1].set_title('Windy Likelihood Table')
axs[3][1].table(cellText=windy_likelihood_table.values, colLabels=windy_likelihood_table.columns, rowLabels = windy_likelihood_table.index, loc='center')

# Display Frequency Tables
axs[0][0].axis('off')
axs[0][0].set_title("Outlook Frequency Table")
axs[0][0].table(cellText=outlook_freq_table.values, colLabels=outlook_freq_table.columns, rowLabels = outlook_freq_table.index, loc='center')
axs[1][0].axis('off')
axs[1][0].set_title('Tempurature Frequency Table')
axs[1][0].table(cellText=temp_freq_table.values, colLabels=temp_freq_table.columns, rowLabels = temp_freq_table.index, loc='center')
axs[2][0].axis('off')
axs[2][0].set_title('Humidity Frequency Table')
axs[2][0].table(cellText=humidity_freq_table.values, colLabels=humidity_freq_table.columns, rowLabels = humidity_freq_table.index, loc='center')
axs[3][0].axis('off')
axs[3][0].set_title('Windy Frequency Table')
axs[3][0].table(cellText=windy_freq_table.values, colLabels=windy_freq_table.columns, rowLabels = windy_freq_table.index, loc='center')

# Display the Posterior Probabilities
output_table = np.hstack((np.round(np.array(probabilities), 2), np.transpose(np.array([y_test]))))
print(output_table)
axs[4][0].axis('off')
axs[4][0].set_title("Posterior Probabilities for Each Class")
t = axs[4][0].table(cellText=output_table, colLabels=['P(Yes) - 0', 'P(No) - 1', "True Value"], loc='center')
t.auto_set_font_size(False)
t.set_fontsize(8)

# Display the Accuracy
acc_output = f"{accuracy * 100:.2f}%"
axs[4][1].axis('off')
axs[4][1].set_title("Accuracy")
t = axs[4][1].table(cellText=[[acc_output]], colLabels=['Accuracy'], loc='center')
t.auto_set_font_size(False)
t.set_fontsize(8)

# Show final board
fig.tight_layout()
plt.show()