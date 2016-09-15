from math import ceil
from string import ascii_lowercase


vocabList = list(ascii_lowercase)
vocabDict = dict(zip(ascii_lowercase, range(26)))

def encrypt(taskInput):
    message = taskInput.split("|")[0]
    lowM, key = taskInput.lower().split("|")
    offset = 0
    encryption = ''
    for i in range(len(message)):
        if lowM[i] not in vocabDict:
            encryption += message[i]
            offset += 1
        else:
            letter = vocabList[(vocabDict[lowM[i]] + vocabDict[key[(i - offset) % len(key)]]) % 26]
            encryption += letter if message[i].islower() else letter.upper()
    return encryption

#ans = "hXpVgGxVt@##USeY^IEbRu*UKQ_bZrV?:u+^ekvDQlfw?N!* h}ZxQ^UHGMAYrTw"
taskInput = "sXxJyEmNx@##KDeG^WWzGm*YAB_bHfN?:s+^tczTBlnk?F!* f}OpU^KSGUOQpIo|PASMICLIWK"
print(encrypt(taskInput))
