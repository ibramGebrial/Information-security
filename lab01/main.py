alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start, shift, direction):
  end_text = ""
  if direction == "decode":
    shift *= -1
  for char in start:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = (position + shift) % 26
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {direction}d result: {end_text}")

def atbash (start):
  end_text = ""  
  for char in start:
      if char in alphabet:
          position = alphabet.index(char)+1
          end_text += alphabet[position*(-1)]        
      else:
        end_text += char

  print(f"Here's the atbash result: {end_text}")

should_continue = True
while should_continue:
  cipher= input("Type 'caesar' to use caesar cipher, type 'atbash'  to use atbash cipher:\n") 
  text = input("Type your message:\n").lower()
  
  if cipher == "caesar":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")  
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start=text, shift=shift, direction=direction)
 
  else:
    atbash(start=text)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_continue = False
    print("Goodbye")
    


