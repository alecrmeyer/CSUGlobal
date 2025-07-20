import random
import nlpaug.augmenter.char as nac

def augment_sentence_word(sentence):
    """
    Augment a sentence by randomly deleting, duplicating, or swapping words.
    """
    sentence = sentence.split(' ')
    num_words = random.randint(1, len(sentence)/2) 
    random_indexes = random.sample(range(len(sentence)), num_words)
    for i in random_indexes:
        ran = random.randint(0, 2)
        if ran == 0 and i < len(sentence): # Randomly delete a word
            del sentence[i]
        elif ran == 1:  # Randomly duplicate a word
            sentence.insert(i, sentence[i])
        elif ran == 2 and i < len(sentence) - 1: # Randomly swap two adjacent words
            tmp = sentence[i]
            sentence[i] = sentence[i+1]
            sentence[i+1] = tmp
    return ' '.join(sentence)

def augment_sentence_char(sentence):
    """
    Augment a sentence by randomly deleting, duplicating, or swapping characters.
    """
    aug = nac.KeyboardAug()
    return aug.augment(sentence)[0]

# Read the raw text data from an unaugmented text file
with open('data_raw.txt', 'r') as file:
    data = file.read()
    data = data.split('.')  

# Randombly choose which type of augmentation to apply to each sentence
# 40% chance for word augmentation, 40% for character augmentation, and 20% no augmentation
augmented_sentence = []
for sentence in data:
    ran = random.random()
    if ran < 0.4:
        sentence = augment_sentence_word(sentence)
    elif ran < 0.8:
        sentence = augment_sentence_char(sentence)
    augmented_sentence.append(sentence)

# Write the augmented text data to a new file
with open('data_augmented.txt', 'w') as file:
    file.write('.'.join(augmented_sentence))