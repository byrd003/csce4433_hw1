def recoverKey(list, input, vocabList, key):
    # set count to 0
    count = 0
    # for each element
    for element in list:
        if element in vocabList: #in vocab
            count +=1 # increment count
    if count == len(list):
        # output
        print("User-specified vocabulary text file: sample.txt")
        print("Key: {}".format(key))
        print("Plaintext message: {}".format(" ".join(list))) # takes plaintext message and joins decrypted words
    else: 
        # decipher text
        decipherText(input,key+1)

def decipherText(input, key):
    # create list to store 
    list = []
    for word in input:
        # set temp string
        tmp = ""
        for each_char in word:
            tmp += chr(ord(each_char)-key) # takes unicode and decrement w key
        list.append(tmp) # throws words together into list
    recoverKey(list, input, vocabList, key)

# setting input 
input = input("User-input ciphertext message: ")
# opening sample.txt (user dict)
with open("sample.txt","r") as f:
    # splits words into readFromDict
    readFromDict = f.read().splitlines()
# adds readFromDict to vocabList
vocabList = " ".join(readFromDict)
input = input.split()
# decipers input split
decipherText(input,1)