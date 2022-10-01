def cipher_transposition():
  text = input("Enter you message: ").replace(" ","").upper()
  key = input("Enter your key: ").upper()
  key_num_list = key_assign_number(key)
  for i in range (len(key)):
    print(key[i], end=" ", flush =True)
  print()

  for i in range (len(key)):
    print(key_num_list[i], end = " ", flush =True)
  print()
  print("------------------")
  letter= len(text)% len(key)
  dummy_char= len(key)- letter

  if letter != 0:
    for i in range(dummy_char):
      text += "a"

  number_of_rows = int(len(text)/ len(key))

  arr = [[0] * len(key) for i in range(number_of_rows)]
  z= 0 
  for i in range(number_of_rows):
    for j in range(len(key)):
      arr[i][j] = text[z]
      z+=1
  
  for i in range(number_of_rows):
    for j in range(len(key)):
      print(arr[i][j], end = " ", flush=True)
    print()
  num_loc =get_location(key,key_num_list)
  cipher_transposition =""
  counter= 0
  for i in range(number_of_rows+1):
    if counter ==len(key):
      break
    else:
      d= int(num_loc[counter])
    for j in range(number_of_rows):
      cipher_transposition += arr[j][d]
    counter+=1

  print("Cipher Text: {} ",format(cipher_transposition))
  
def get_location(key, key_num_list):
  num_loc=""
  for i in range(len(key)+1):
    for j in range(len(key)):
      if key_num_list[j] ==i:
        num_loc += str(j)
  return num_loc      
def key_assign_number(key):
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  key_num_list=list(range(len(key)))
  init =0
  for i in range(len(alphabet)):
    for j in range(len(key)):
      if alphabet[i]== key[j]:
        init+=1
        key_num_list[j]= init
  return key_num_list

cipher_transposition()'''

from random import choice, randint
from collections import Counter

text = "HelloWorld"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
  key= [randint(1,20) for x in range(len(text))]
  count = Counter(key)
  switch =0;
  n=0
  for l in count:
    if count[key[n]] > 1:
      switch = 1
      break
    n += 1
  if switch == 0:
    break

key.sort()
print("key: ",key)

grille = [choice(alphabet) for x in range(0,21)]

n=0
for i in range(len(grille)):
  if n < len(text):
    if i == key[n]:
      grille[i] = text[n]
      n+=1
print()
for j in range(0,6):
	if j == 0:
		print(" ", end = "    ")
	else:
		print(j, end = "   ")
print()

n = 1

for j in range(1,len(grille)):
	if j == 1:
		print(n, end = "  | "); n += 1
		print(grille[j], end = " | ")
	elif j % 5 != 0:
		print(grille[j], end = " | ")
	else:
		print(grille[j], end = " | ")
		print()
		if n < 5:
			print(n, end = "  | "); n += 1
print()



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def vinenere(start,key):
  key*= len(start)

  end_text=""
  for i,j in enumerate(start):
    position = alphabet.index(j)
    position_key = alphabet.index(key[i])
    new_posiotion = (position+position_key)%26
    end_text +=alphabet[new_posiotion]
  print(f"our result: {end_text}")

vinenere("hello ".replace(' ', ''), "bic")'''