#luke\doc\coding
#Transposition Cypher Encryption

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)
    #Print the encrypted string in ciphertext to the screen, with
    #a '|' (pipe character) after it in case there are spaces at
    #the end of the encrypted message.
    print(ciphertext + '|')

    #Copies the encrypted string in ciphertext to the clipboard.
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    #Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    #Loop through each column in ciphertext.
    for col in range(key):
        pointer = col

        #Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
            #Place the character at pointer in message at the
            #current column in the ciphertext list.
            ciphertext[col] += message[pointer]

            #move pointer over
            pointer += key

    #Convert the ciphertext list into a single string value and return it.
    return''.join (ciphertext)

if __name__ == '__main__':
    main()
