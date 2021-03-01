def is_letter(x): #έλεγχος αν ο χαρακτήρας είναι γράμμα
        syn = False
        y=ord(x)
        for i in range(65,91): # κεφαλαία λατινικά
            if(y==i):
                syn=True
        for i in range(97,123): # πεζά λατινικά
            if(y==i):
                syn=True
        return syn

with open('D:/!CODE/PYTHON/two_cities_ascii.txt', 'r') as file:
    keimeno = file.read()
    stoixeia=len(keimeno)
    count_letter=0
    count_no_letter=0
    lexeis=[]
    for i in range (0,stoixeia):
        if (is_letter(keimeno[i])):
            count_no_letter=0
            count_letter += 1
            if (count_letter==1):
                arxh=i
        else:
            count_no_letter += 1
            if (count_no_letter==1 and count_letter!=0 ):
                count_letter=0
                telos=i
                lexeis.append(keimeno[arxh:telos])
    if(count_letter!=0):
        telos=i
        lexeis.append(keimeno[arxh:telos+1])
#για κάθε λέξη ελέγχω όλα τα πιθανά ζευγάρια και εμφανίζω τα ζευγάρια λέξεων
# με σύνολο χαρακτήρων = 20
    kena = []
    while len(lexeis) >1:
        print(len(lexeis))
        syn=False
        for i in range (1,len(lexeis)):
            if(len(lexeis[0])+len(lexeis[i])==20):
                print(lexeis[0],"+",lexeis[i])
                lexeis.pop(i)
                lexeis.pop(0)
                #print(lexeis)
                syn= True
                break
        if(syn==False):
            print(lexeis[0])
            kena.append(lexeis[0])
            lexeis.pop(0)

            #print(lexeis)
    if  len(lexeis)!=0:
        print(lexeis[0])
        kena.append(lexeis[0])
        lexeis.pop(0)

    print(kena)
