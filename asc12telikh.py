str.encode("ascii")
with open('D:/!CODE/PYTHON/asc.txt', 'rt') as file:
    keimeno = file.read()
    stoixeia=len(keimeno)
    keimeno2=[]
    for x in keimeno:
            y=128-ord(x)
            keimeno2.append(chr(y))
    #print(keimeno2)
    keimeno2.reverse()
    print(keimeno2)
