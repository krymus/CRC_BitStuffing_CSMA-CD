DIVISOR = '101010'
DIVISOR_LENGTH = len(DIVISOR)

file = open('stream.txt', 'r')

s = file.read()

messages = []

message = ''

def XOR( a, b):
    a = str(a)
    b = str(b)
    if a == b:
        return '0'
    return '1'

def remainder(message):
    n = len(message)
    letters = []
    for i in range(n):
        letters.append(message[i])
    

    for i in range(n - (DIVISOR_LENGTH - 1)):
        if letters[i] == '1':
            for j in range(DIVISOR_LENGTH):
                letters[i+j] = XOR(letters[i+j], DIVISOR[j])
        

    remainder = ''
    for i in range(n - DIVISOR_LENGTH + 1, n):
        if(i<0):
            for i in range(len(letters)):
                remainder += letters[i]
            return remainder
        remainder = remainder + letters[i]
    return remainder
        

def CRC(message):
    for i in range(DIVISOR_LENGTH-1):
        message = message + '0'
    return remainder(message)

def unBitStuffing(message):
    result = ''
    counter = 0
    skip = False

    for i in range(len(message)):
        if(skip):
            skip = False
            continue

        if(message[i] == '1'):
            counter += 1
        else:
            counter = 0

        if(counter == 5):
            skip = True
            counter = 0

        result = result + message[i]

    return result

def checkCRC(message):
    if(message == ''):
        return False
    givenRemainder = ''
    msg = ''
    readLetters = True
    
    for i in range(len(message)):
        if(i == len(message) - DIVISOR_LENGTH + 1):
            readLetters = False
        if(readLetters):
            msg += message[i]
        else:
            givenRemainder += message[i]


    for i in range(DIVISOR_LENGTH-1):
        msg = msg + '0'
    calculatedRemainder = remainder(msg)
    if(givenRemainder == calculatedRemainder):
        return True
    else:
        print("givenRemainder: " + str(givenRemainder) + "calculatedRemainder: " + str(calculatedRemainder))
        return False


def readStream(s):
    receivingMessage = False
    result = ''
    signalHelp = 0
    for i in range (len(s)):
        if(not signalHelp == 0):
            signalHelp = signalHelp - 1
            continue

        if(i < len(s) - 7 and s[i] == '0' and s[i+1] == '1' and s[i+2] == '1' and 
        s[i+3] == '1' and s[i+4] == '1' and s[i+5] == '1' and 
        s[i+6] == '1' and s[i+7] == '0'):
            if(receivingMessage):
                print("original message: " + result)
                result = unBitStuffing(result)
                print("unbitstuffed message: " + result)

                if(checkCRC(result) == True):
                    noCRCmsg = ''
                    for i in range(len(result) - DIVISOR_LENGTH + 1):
                        noCRCmsg += result[i]
                    messages.append(noCRCmsg)
                    print("noCRCmsg: " + noCRCmsg)
                    print("Message accepted")
                else:
                    messages.append("Message error")
                    receivingMessage = False
                    print("Message rejected")
                
                result = ''

            signalHelp = 7
            receivingMessage = not receivingMessage

        if(receivingMessage and signalHelp == 0):
            result += s[i]
        


        

readStream(s)

print("Printing messages: ")
for i in messages:
    print(i)

file.close()