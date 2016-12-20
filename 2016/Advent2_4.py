from collections import Counter
import string

sum_of_sectors=0

def is_real(stanza):
    stanza =sorted(stanza)
    #print(stanza)
    freq = sorted(Counter(stanza).most_common(100), key= lambda elem:(-elem[1],elem[0]))
    #print(freq)
    i=0
    answers = ""
    for key,val in freq:
       if i<5:
        answers += key
       i+=1
    #print("RISPOSTA: " + answers)
    return answers 

def cifrario_di_Cesare(giri):
    alfabeto = string.ascii_lowercase
    decode = giri % len(alfabeto)
    return str.maketrans(alfabeto, alfabeto[decode:] + alfabeto[:decode])

n_camere_uguali = 0
with open('input2_es4.txt') as file:
    for row in file.readlines():
        row.rstrip()
        row.lstrip()
        riga = row.replace(r' ','').strip()
        checksum =riga[-7:].replace(r']','').replace(r'[','').replace(r"\s+",'').replace(r"\t",'').replace(r"\n",'').strip()
        sector = riga[-11:-7].replace(r']','').replace(r'[','').replace(r'-','').strip()
        room_name_encode = riga[:-11].strip()
        room_encr = riga[:-11].replace(r'-','').strip()
        risposta = is_real(room_encr).strip()
        # print("------------RIGA : " + riga + "------------------------------" )
        # print("RISPOSTA : " + risposta)
        # print("CHECKSUM : " + checksum)
        # print("SECTOR : " + sector)
        # print("ROOM ENCRIPT CODE : " + room_encr)
        if (str(risposta).replace(r' ','')==str(checksum).replace(r' ','').strip()):
            # print("UGUALI!!")
            sum_of_sectors += int(sector)
            room_name_decode = room_name_encode.translate(cifrario_di_Cesare(int(sector)))
            print("ROOM NAME ENCODE: " + room_name_encode)
            print("ROOM NAME DECODE: " + room_name_decode)
            if 'north' in room_name_decode:
                print("*****************" + sector + " NAME : " + room_name_decode)
        # else:
            # print("DIVERSI!!")
        # print("SOMMA : " + str(sum_of_sectors))
    print("*********** SOMMA SETTORI = " + str(sum_of_sectors) + "*************************")