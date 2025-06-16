import csv
import random


options = ["Land","Card Advnatage","Interaction","Creature","Ramp","Keep"]

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
with open('/Users/alecrmeyer/Desktop/CSUGlobal/repo/CSUGlobal/CSC510/Portfolio/data.csv', 'a', newline='') as file:
    writer = csv.writer(file)   
    while(True):
        # num_cards = random.randint(5, 7)
        num_cards = 7
        hand = []
        numbers = random.sample(range(0, 59), num_cards)
        for num in numbers:
            hand.append(deck[num])
        keep = input(str(hand) + "\nKeep? (y/n)")
        
        hand_csv = to_csv_format(hand)

        if keep == 'y':
            hand_csv.append(1)
        elif keep == 'n':
            hand_csv.append(0)
        else:
            break
        print(hand_csv)
        writer.writerow(hand_csv)   
    










    """
    Land,Card Advnatage,Interaction,Creature,Ramp,Keep
0,6,1,0,0,0
0,6,0,1,0,0
2,2,1,2,0,1
3,2,2,0,0,1
5,0,2,0,0,0
6,1,0,0,0,0
6,0,1,0,0,0
4,2,1,0,0,1
4,0,2,1,0,0
3,4,0,0,0,1
3,0,2,2,0,1
5,1,1,0,0,0
5,1,0,1,0,0
5,0,1,1,0,0
5,2,0,0,0,0
5,0,2,0,0,0
5,0,0,2,0,0
1,0,4,2,0,0
1,0,2,3,0,0
1,2,2,2,0,1
1,3,2,1,0,1
1,3,1,2,0,1
1,3,3,0,0,1
1,2,3,1,0,1
2,2,3,0,0,1
2,4,0,1,0,1
2,0,0,5,0,0
1,0,6,0,0,0
1,0,3,3,0,0
1,0,2,4,0,0
1,0,0,6,0,0
6,0,0,0,1,0
1,1,1,1,3,0
2,1,1,1,2,1
3,1,0,1,2,0
4,0,3,0,0,0
5,0,1,0,1,0
2,1,2,2,0,1
0,2,3,0,2,0
0,1,1,1,4,0
0,3,1,1,2,0
0,0,0,1,6,0
""" 