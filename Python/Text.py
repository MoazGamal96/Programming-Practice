import csv
import random
from asyncore import read

with open('500 Words.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
     sentence = random.choice(reader)
    print(sentence)