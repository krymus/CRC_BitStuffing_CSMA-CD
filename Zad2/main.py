import random
import time

medium = [0] * 30
state = []

noMessages1 = 3
noMessages2 = 3
tries1 = 0
tries2 = 0

issending1 = False
issending2 = False

start1 = 0
end1 = 0

start2 = 29
end2 = 29

def collision(node):
    if(node == 1):
        if(state[0] == 1):
            return False
        else:
            return True
    else:
        if(state[29] == 2):
            return False
        else:
            return True 
        
def mediumFree(node):
    if(node == 1):
        if(state[0] == 0):
            return True
        else:
            return False
    else:
        if(state[29] == 0):
            return True
        else:
            return False
    

checkpoint1 = 0
clear1 = 0
checkpoint2 = 29
clear2= 29
sent1 = 0
sent2 = 0

while(noMessages1 > 0 or noMessages2 > 0):
    
    state.clear()

    #assigning state of medium
    for i in medium:
        state.append(i)
    

    #   STATION ONE
    if(issending1): 
        if(collision(1)): #if collision appeared
            print("collision on 1")
            issending1 = False
            checkpoint1 = start1
            start1 = 0
            sent1 = 0
        else: 
            if(start1<29): #if message couldnt get to receiver so far
                start1 += 1
                medium[start1] += 1
            elif(sent1<30): #counting messages that could be received
                sent1 += 1
            else:
                print("message accepted") #accepting message
                issending1 = False
                checkpoint1 = 29
                start1 = 0
                sent1 = 0
                tries1 = 0
                noMessages1 -= 1

    #   MEDIUM OPERATIONS
    if(checkpoint1 != clear1): 
        if(checkpoint1 < 29):
            checkpoint1 += 1
            medium[checkpoint1] += 1
            medium[clear1] -= 1
            clear1 += 1
        else:
            medium[clear1] -= 1
            clear1 += 1
    elif(checkpoint1 != 0):
        medium[checkpoint1] -= 1
        checkpoint1 = 0
        clear1 = 0

    #   IF STATION ONE IS NOT BORADCASTING  
    elif(mediumFree(1) and noMessages1 > 0): # draw whether to start broadcasting
        if(random.randint(1, 2**tries1) == 1):
            tries1 += 1
            print("1 starts sending")
            issending1 = True
            medium[0] += 1



#   STATION TWO
    if(issending2): 
        if(collision(2)): #if collision appeared
            print("collision on 2")
            issending2 = False
            checkpoint2 = start2
            start2 = 29
            sent2 = 0
        else: 
            if(start2>0): #if message couldnt get to receiver so far
                start2 -= 1
                medium[start2] += 2
            elif(sent2<30): #counting messages that could be received
                sent2 += 1
            else:
                print("message accepted") #accepting message
                issending2 = False
                checkpoint2 = 0
                start2 = 29
                sent2 = 0
                tries2 = 0
                noMessages2 -= 1

     #   MEDIUM OPERATIONS
    if(checkpoint2 != clear2): 

        if(checkpoint2 > 0):
            checkpoint2 -= 1
            medium[checkpoint2] += 2
            medium[clear2] -= 2
            clear2 -= 1
        else:
            medium[clear2] -= 2
            clear2 -= 1
    elif(checkpoint2 != 29):
        medium[checkpoint2] -= 2
        checkpoint2 = 29
        clear2 = 29

    #   IF STATION TWO IS NOT BORADCASTING  
    elif(mediumFree(2) and noMessages2 > 0): # draw whether to start broadcasting
        if(random.randint(1, 2**tries2) == 1):
            tries2 += 1
            print("2 starts sending")
            issending2 = True
            medium[29] += 2



    
    
    #printing medium state
    for i in medium:
        if( i == 0):
            print("\033[92m0\033[0m", end = ' ') 
        elif( i == 1):
            print("\033[34m1\033[0m", end = ' ') 
        elif( i == 2):
            print("\033[33m2\033[0m", end = ' ') 
        elif( i == 3):
            print("\033[31m3\033[0m", end = ' ') 
    print("")
    time.sleep(0.01)
    
    







