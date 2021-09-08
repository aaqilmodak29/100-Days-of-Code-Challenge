import art
print(art.logo)
alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cont = True
while cont == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(txt, shft, dire):
    if direction == "encode":
      y = 0
      encrypted = []
      for char in txt:
        if char in alphabet:
          x = alphabet.index(text[y])
          y += 1
          shifted_num = x + shift
          if shifted_num > 25:
            shifted_num = (shifted_num + (shift - 1))%len(alphabet)
          encrypted.append(alphabet[shifted_num])
          joint_list = ''.join(encrypted)
        else:
          encrypted.append(char)
          joint_list = ''.join(encrypted)
      print(joint_list)
      
    elif direction == "decode":
      y = 0
      decrypted = []
      for char in txt:
        if char in alphabet:
          x = alphabet.index(text[y])
          y += 1
          shifted_num = x - shift
          decrypted.append(alphabet[shifted_num])
          joint_list = ''.join(decrypted)
        else:
          decrypted.append(char)
          joint_list = ''.join(decrypted)
      print(joint_list)
    
    else:
        print("Wrong Input, type either 'encode' or 'decode'.")

  caesar(txt = text, shft = shift, dire = direction)
  z = input("Type 'yes' to continue or 'no' to stop: ").lower()
  if z == "no":
    cont = False
