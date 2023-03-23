from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print("\n==========================================================================")  
  print(f"        Here's the {cipher_direction}d result: {end_text}")
  print("==========================================================================\n")

def coding():
  while True:
    print("\n--------------------------------------------------------------------------")  
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if direction == 'decode' or direction == 'encode':
      break      
    else:
      print("\nInvalid input.")
      print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

  print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
  text = input("Type your message:\n\n").lower()
  print("──────────────────────────────────────────────────────────────────────────")
  while True:
    try:
        shift = int(input("\nType the shift number: "))
        break
    except ValueError:
      print("\nPlease enter a number.")
      print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
  shift = shift % 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

coding()

while True:
  output = input("Type 'y' if you want to go again. Otherwise type 'n': ").lower()
  
  if output == 'y':
    coding()
  elif output == 'n':
    print("\nGoodbye!")
    print("¨¨¨¨¨¨¨¨")
    break
  else:
    print("\nIncorrect input.")
    print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")