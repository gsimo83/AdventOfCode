from collections import Counter
matrix = []
tupla = []
password = ""
with open('input2_es6.txt') as f:
    #f.read().replace('\n','')
    for row in f.readlines():
        #row.rstrip().replace('\n','')
        for char in row:
            tupla.append(char)
        matrix.append(tupla)
        tupla = []
    #print(matrix)
    matrix = list(zip(*matrix[::-1]))
    #print(matrix)
    for riga in matrix:
        freq = sorted(Counter(riga).most_common(1))
        for key,val in freq:
            password += key
        #print("Carattere piu' frequente : " + freq)
        #password.append(freq)
    print("PASSWORD :" + str(password))
    nuova_passord = ""
    password=""
    min_val = 1000
    for riga in matrix:
        print(riga)
        freq = sorted(Counter(riga).most_common(1000), key= lambda elem:(elem[0]))
        for key,val in freq:
            if val<=min_val:
                min_val=val
        for k,v in freq:
            if v==min_val:
                password+=k        
        min_val=1000
        print(password)
        password= sorted(password)
        print(password)
        nuova_passord += password[0]
        password=""
    print(nuova_passord)