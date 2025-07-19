import random
import nlpaug
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.char as nac
with open('data_raw.txt', 'r') as file:
    data = file.read()
    data = data.split('.')  

def augment_sentence_word(sentence):
    sentence = sentence.split(' ')
    num_words = random.randint(1, len(sentence)/2) 
    random_indexes = random.sample(range(len(sentence)), num_words)
    for i in random_indexes:
        ran = random.randint(3, 3)
        if ran == 0:
            del sentence[i]
        elif ran == 1:  
            sentence.insert(i, sentence[i])
        elif ran == 2:
            tmp = sentence[i]
            sentence[i] = sentence[i+1]
            sentence[i+1] = tmp
    return ' '.join(sentence)

def augment_sentence_char(sentence):
    aug = nac.KeyboardAug()
    return aug.augment(sentence)

data[0] = augment_sentence_word(data[0])
data[1] = augment_sentence_char(data[1])[0]

print(data)