import math
with open('D:/!CODE/PYTHON/asc.txt', 'r') as file:
    keimeno = file.read()


    # δημιουργεία πίνακα με τους μονούς κωδικούς ASCII
    arh=[]
    for x in keimeno:
        y=ord(x)
        if(y%2==1):
            arh.append(y)
            

    stoixeia=len(arh)
    # δημιουργεία πίνακα με το πλήθος εμφανίσεων των κωδικών
    poso=[]
    for i in range (0,128):
        poso.append(0)

    for i in range (0,stoixeia):
            poso[arh[i]]+=1

    for i in range (0,128):
        if(poso[i]!=0):
            pososto=poso[i]*100/stoixeia
            fores=math.ceil(pososto)
            print(chr(i),fores*"*")
