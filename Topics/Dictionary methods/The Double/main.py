# put your python code here
from string import ascii_lowercase
alphabet = list(ascii_lowercase)
alphabet_2 = []
for i in range(0, 26):
    alphabet_2.append(alphabet[i]*2)

double_alphabet = dict.fromkeys(ascii_lowercase)
i = 0
for key in double_alphabet:
    double_alphabet[key] = alphabet_2[i]
    i = i+1