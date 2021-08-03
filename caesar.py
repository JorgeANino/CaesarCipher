import sys

def caesars_encrypt(plain_text, k):
   cipher_text = ""
   for character in plain_text:
      if character.isalpha():
         if character.isupper():
            cipher_text += chr((ord(character) + k - 65) % 26 + 65)
         else:
            cipher_text += chr((ord(character) + k - 97) % 26 + 97)
      else:
         cipher_text += character
   return cipher_text

def main(argv):
   k = 0
   if len(argv) != 1:
      print("Usage: python caesar.py k")
      sys.exit(-1)
   k = int(argv[0])
   plain_text = input("plaintext: ")
   cipher_text = caesars_encrypt(plain_text, k)
   print("ciphertext: " + cipher_text)

if __name__ == "__main__":
   main(sys.argv[1:])