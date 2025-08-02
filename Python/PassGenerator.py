
import random
import string

S1 =list(string.ascii_lowercase)
S2 = list(string.ascii_uppercase)
S3 = list(string.digits)
S4 = list(string.punctuation)

char_num = input ('number of pass charachters: ')
while True:
    try:
        char_num = int(char_num)
        if char_num < 6 :
            print("put more than 6 chars")
            char_num = input ("please enter numbere again: ")
        else:
                break
    except: 
        print("please enter numbers only")
        char_num = input( "how many charachters?: ")

random.shuffle(S1)
random.shuffle(S2)
random.shuffle(S3)
random.shuffle(S4)
 
part1 = round(char_num * (30/100)) 
part2 = round(char_num * (20/100)) 

passowrd = []
for i in range(part1):
    passowrd.append(S1[i])
    passowrd.append(S2[i])

for i in range(part2):
    passowrd.append(S3[i])
    passowrd.append(S4[i])
passowrd = "".join(passowrd[0:])
print(passowrd)