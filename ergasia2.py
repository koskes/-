fin = open ("words.txt","r")
vowels = ['a', 'e', 'i', 'o', 'u']
badlet = ['f','c','k','r']
for line in fin:
    line=line.strip()
    words=line.split()
    for y in words:
        grammata=[]
        newvowels=[]
        newbadlet=[]
        for p in y:
            if p in vowels:
                newvowels.append(p)
            elif p in badlet:
                newbadlet.append(p)
                newbadlet=list(set(newbadlet))
            else:
                grammata.append(p)
                grammata=list(set(grammata))
    if len(newbadlet) > len(grammata) :
        print ("η",y,"ειναι κακη λεξη")
    elif len(grammata) > len(newbadlet):
        print ("η",y,"ειναι καλη λεξη")
    else:
        print("η",y," έχει ελλειπη στοιχεια")
  
