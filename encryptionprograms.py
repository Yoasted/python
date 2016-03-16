#!luke/bin/python
#EncryptionPrograms v.01

import pyperclip

def menu():
    #To be extended with more types of encryptions
    print((("""
-----------------------------------------------
1. Caesar Cipher
-----------------------------------------------
""")))

    choice = int(input("\nChoose which encryption type you want: "))

    #Sends the user to the encryption for menu for using a specific cipher.
    if choice == 1:
        caesarcipher()

    elif choice == 2:
        transpocipher()

    else:
        menu()


def caesarcipher():
    mode = int(input("Do you want to encrypt or decrypt a message? 1 or 2: "))

    
    #String to be encrypted:
    message = input("Input the message you want [en/de]crypted: ")

    #Input the key
    key = int(input("Input the key : "))

    #Every possible symbol that can be encrypted.
    CHARACTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

    #Stores the encrypted form of the string.
    translated = ''

    #Capitalizes the string in the message.
    #message = message.upper()

    for char in message:
        if char in CHARACTERS:
            #Gets the encrypted/decrypted number for the symbol.
            num = CHARACTERS.find(char)#gets the number of the symbol.

            #encrypt
            if mode == 1:
                num = num + key

            #decrypt
            elif mode == 2:
                num = num - key

            #handles wrap-around if num is larger than the length of CHARACTERS
            #or less than 0.

            if num >= len(CHARACTERS):
                num = num - len(CHARACTERS)
            elif num < 0:
                num = num + len(CHARACTERS)

            #Add encrypted number's symbol at the end of translated string.
            translated = translated + CHARACTERS[num]

        else:
            #adds the symbol without encryption
            translated = translated + symbol

    #Prints the encrypted/decrypted string to the clipboard.
    print("Translated string: " + translated.upper())
    

    #Copies the encrypted/decrypted string to the clipboard.
    pyperclip.copy(translated)
    print("\n\nCOPIED TO CLIPBOARD!")

    print("\nReturning to Main Menu.\n\n")
    menu()
    
menu()
        


                
