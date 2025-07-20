This Python script will take an input file named "data_raw.txt" and will output an augmented text file named "data_augmented.txt". 
The data augmentation process in this file can be broken down into word augmentation and character augmentation. For the word 
augmentation, the script will randomly delete, duplicate or swap two words. The character augmentation uses the nlpaug library
and will simulate typos by replacing characters with adjacent characters on a keyboard. These two techniques then have a 40% each 
to be performed on a sentence and there is a 20% chance the sentence is untouched. using these two methods together provides a 
robust method of text augmentation which will allow for improved training on any text based machine learning model. 