DIVISOR = '101010'
DIVISOR_LENGTH = len(DIVISOR)

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
        remainder = remainder + letters[i]
    return remainder

def CRC(message):
    for i in range(DIVISOR_LENGTH-1):
        message = message + '0'
    return remainder(message)

def addSTARTEND(message):
    letters = []

    letters.append('0')
    for i in range(6):
        letters.append('1')
    letters.append('0')

    for i in range(len(message)):
        letters.append(message[i])
    
    letters.append('0')
    for i in range(6):
        letters.append('1')
    letters.append('0')

    result = ''
    for i in range(len(letters)):
        result = result + letters[i]
    
    return result
        
def bitStuffing(message):
    result = ''
    counter = 0

    for i in range(len(message)):
        x = message[i]

        if(x == '1'):
            counter +=1
        else:
            counter = 0

        result += message[i]

        if(counter == 5):
            result += '0'
            counter = 0

    return result


def sendMessage(message):
    message = message + CRC(message)
    print("Message with CRC: " + message)
    message = bitStuffing(message)
    print("Message with bitstuffing: " + message)
    message = addSTARTEND(message)
    print("Message with STARTEND: " + message)

    file = open("stream.txt", 'a')
    file.write(message)
    file.close()
    
    


sendMessage('0101011111111111111111111111111111')
sendMessage('1001111111111111110000001111111011')
sendMessage('0000000000000011111111100000011100')
sendMessage('1010111111110101010101010010101010')

    
