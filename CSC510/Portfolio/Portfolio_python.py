import numpy as np
import pandas as pd
import random

data = pd.read_csv("data.csv")

from sklearn.model_selection import train_test_split
df = pd.DataFrame(data)

X = df[["Land", "Card Advnatage", "Interaction", "Creature", "Ramp"]]
y = df["Keep"]
X = X.to_numpy()
y = y.to_numpy().reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state = 25)

def expert_system_prediction(hand, prediction):
    """
    expert_activation_function takes in a sample hand and its prediction, 
    and returns a new prediction if the system determines the initial prediction
    was not correct
    
    :param hand:         input hand to verify
    :param prediction:   initial prediction
    """
    land = hand[0]
    creature = hand[1]
    card_adv = hand[2]
    interaction = hand[3]
    ramp = hand[4]    

    if land == 0:
        return 0
    elif land > 4:
        return 0
    
    if land == 1:
        if card_adv < 2:
            return 0
        elif ramp < 1:
            return 0

    if land + ramp > 5:
        return 0
    return prediction


def activation_function(x):
    """
    output_activation_function applies the sigmoid activation function 
    
    :param x: input data
    """
    return 1 / (1 + np.exp(-x))

def activation_derivative(x):
    """
    output_activation_function applies the sigmoid activation function derivative 
    
    :param x: input data
    """
    return activation_function(x) * (1 - activation_function(x))

def feedforward(X, w_input_to_hidden, b_input_to_hidden, w_hidden_to_output, b_hidden_to_output):
    """
    feedforward returns the otputs of the activation function applied on the weight X feature + the bias
    a = f(wp + b)

    :X:                 input training data
    :w_input_to_hidden: weights used between the input and hidden layer
    :b_input_to_hidden: bias used between the input and hidden layer
    :w_hidden_to_output: weights used between the hidden and output layer
    :b_hidden_to_output: bias used between the hidden and output layer
    """
    z_input = np.dot(X, w_input_to_hidden) + b_input_to_hidden

    a_input = activation_function(z_input)

    z_hidden = np.dot(a_input, w_hidden_to_output) + b_hidden_to_output
    a_hidden = activation_function(z_hidden)
    return a_input, a_hidden

hidden_Layer_neurons = 3
output_neruons = 1

# Initialize weights
w_input_to_hidden = np.random.uniform(size=(X_train.shape[1], hidden_Layer_neurons))
w_hidden_to_output = np.random.uniform(size=(hidden_Layer_neurons, output_neruons))

b_input_to_hidden = np.zeros((1, hidden_Layer_neurons))
b_hidden_to_output = np.zeros((1, output_neruons))

learning_rate = .01
epochs = 10000
for x in range(epochs):
    a_input, a_hidden = feedforward(X_train, w_input_to_hidden, b_input_to_hidden, w_hidden_to_output, b_hidden_to_output)

    #=== Back Propagation ===#
    error_output = y_train - a_hidden
    delta_output = error_output * activation_derivative(a_hidden)

    # delta weight = eta X 
    hidden_layer_delta = np.dot(delta_output, w_hidden_to_output.T) * activation_derivative(a_input)

    w_hidden_to_output += np.dot(a_input.T, delta_output) * learning_rate
    b_input_to_hidden += np.sum(delta_output) * learning_rate

    w_input_to_hidden += np.dot(X_train.T, hidden_layer_delta) * learning_rate
    b_hidden_to_output += np.sum(delta_output) * learning_rate



# Random Forest
from sklearn.ensemble import RandomForestClassifier
rf_clf = RandomForestClassifier(max_depth=2, random_state=0)
rf_clf.fit(X_train, y_train.reshape(1, -1)[0])

# Logistic 
from sklearn.linear_model import LogisticRegression
log_clf = LogisticRegression(random_state=0).fit(X_train, y_train.reshape(1, -1)[0])



# UI
options = ["Land","Card Advnatage","Interaction","Creature","Ramp","Keep"]
options_simple = ["l","a","i","c","r","Keep"]

def to_csv_format(hand):
    ret = [0] * 5
    for card in hand:
        ret[options.index(card)] += 1
    return ret

land_list = [options[0]] * 20
draw_list = [options[1]] * 12
inter_list = [options[2]] * 12
creat_list = [options[3]] * 12
ramp_list = [options[4]] * 4
deck = land_list + draw_list + inter_list + creat_list + ramp_list

while(True):
    hand = []
    hand_text = []
    type_of_sample = input("""Please select an option: 
        1. Enter a hand (1)
        2. Generate a random hand (2)
        3. Type any other character to end
        """)
    if type_of_sample == "1":
        hand_raw = input("""Enter a sample hand of 7 Magic: The Gathering cards separated by a comma where:
                        l - Land
                        a - Card Advantage
                        i - Interaction
                        c - Creature
                        r - Ramp
                        (e.g. \"l,l,a,i,c,c,r)\"
                        Hand: """)  
        hand = [0] * 5
        for card in hand_raw.split(","):
            hand[options_simple.index(card)] += 1
            hand_text.append(options[options_simple.index(card)])
        

    elif type_of_sample == "2":
        numbers = random.sample(range(0, 59), 7)
        for num in numbers:
            hand.append(deck[num])
        hand_text = hand
        hand = to_csv_format(hand)
        
    else:
        print("Ending program")
        break

    a_input, a_hidden = feedforward(hand, w_input_to_hidden, b_input_to_hidden, w_hidden_to_output, b_hidden_to_output)    
    nn_pred = a_hidden > 0.5

    # Expert system + Artificial Neural Network
    expert_pred = expert_system_prediction(hand, nn_pred[0][0])

    hand = [hand] # Format for sklearn models
    rf_pred = rf_clf.predict(np.array(hand))
    log_pred = log_clf.predict(np.array(hand))

    def bin_to_val(bin):
        if bin == 1:
            return "Keep"
        else:
            return "Mulligan"
    print()
    print("Input hand: " + str(hand_text))
    print("Logistic Regression:               " + str(bin_to_val(log_pred[0])))
    print("Random Forest:                     " + str(bin_to_val(rf_pred[0])))
    print("Artificial Neural Network Pred:    " + str(bin_to_val(nn_pred[0][0])))
    print("ANN + Expert System:               " + str(bin_to_val(expert_pred)))
    print()













