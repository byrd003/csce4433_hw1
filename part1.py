# set max key value size due to alphabet constraint
keyMaxVal = 26

# function for setting mode for input
def setActionType():
    while True: 
        # uer input for action type to take on message 
        print("Do you wish to encrypt or decrypt a message?")
        print("Type 'e' for encrypt or 'd' for decrypt")
        action = input().lower()
        if action in 'e d'.split():
            # takes action
            return action
        else:
            # error handling for input
            print('Enter either "e" or "d"')

def getMessage():
    # gets msg from user to use
    print("User-input message: ")
    return input()

def genKey():
    # generates key based on user input
    key = 0
    while True:
    
        print("User-input key (1-%s): "%(keyMaxVal))
        key = int(input()) # gets key

        #check if key is within restraint
        if (key>= 1 and key <= keyMaxVal):
            return key

# generates msg based on e or d
def genMsg(action,msg,key):
    # if d, you want to decrement k
    if action[0] == "d":
        key = -key
    # setting str variable for translated msg
    translatedMsg =""

    # for each character
    for char in msg:
        # if alpha
        if char.isalpha():
            # sets char to unicode val
            uni = ord(char)
            # will increment with key 
            uni += key 
            # if upper case
            if char.isupper():
                # if uni value gt Z
                if uni> ord('Z'):
                    # uni decrements from Z
                    uni -= 26
                # if uni value lt A
                elif uni < ord('A'):
                    # increment 
                    uni += 26
            # lower case
            elif char.islower():
                if uni > ord('z'): # uni decrements from Z if gt uni
                    uni -= 26
                # uni increments from a if lt
                elif uni < ord('a'): 
                    uni += 26  
            # sets uni to translated message
            translatedMsg += chr(uni)
        else:
            translatedMsg += char
    return translatedMsg

# action items to be done
action = setActionType() # set mode
msg = getMessage() # set message
key = genKey() # set key

# output
print("Output: " + genMsg(action, msg, key))
