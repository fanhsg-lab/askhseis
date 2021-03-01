import random

#εισαγωγή διαστάσεων πίνακα
x=int(input("give x"))
y=int(input("give y"))
S=0
for g in range(100):
    p=[]

    #δημιουργία πίνακα
    for i in range(x):
        s=[]
        for j in range(y):
            s.append("O")
        p.append(s)

    #print(p)

    syn=x*y #υπολογισμός πλήθους θέσεων
    s=round(syn/2) #πλήθος S
    for k in range(s):
        done=False
        while(done==False): # όσο σε μία νέα θέση να εισαχθεί το "S"
            xi = random.randint(0, x-1)
            yi = random.randint(0, y-1)
            if (p[xi][yi]!="S" ):
                p[xi][yi]="S"
                done=True

    #print(p)

    count=0 #πλήθος "SOS"
    for i in range(x):
        for j in range(y):
            if(j<y-2): #οριζόντιος έλεγχος
                if (p[i][j]=="S"):
                    if(p[i][j+1]=="O" and p[i][j+2]=="S"):
                        count+=1
            if(i<x-2): #κάθετος έλεγχος
                if (p[i][j]=="S"):
                    if(p[i+1][j]=="O" and p[i+2][j]=="S"):
                        count+=1
                if(j<y-2): #διαγώνιος(πάνω αριστερ΄ά κάτω δεξιά) έλεγχος
                    if (p[i][j]=="S"):
                        if(p[i+1][j+1]=="O" and p[i+2][j+2]=="S"):
                            count+=1
                if(j>=2): #διαγώνιος(πάνω δεξιά κάτω αριστερά) έλεγχος
                    if (p[i][j]=="S"):
                        if(p[i+1][j-1]=="O" and p[i+2][j-2]=="S"):
                            count+=1
    S=S+count
mo=S/100
print("pososto = ",mo)
