import tkinter
import cmath
import string
import math
import random
    #DZIAŁA 
def fenceCipher(string=None, key=None):
    """Funkcja szyfrujaca podany ciag znakow za pomoca szyfru ogrodzeniowego.
    
    Args:
        string (str, optional): Ciag znakow do szyfrowania. Defaults to None.
        key (int, optional): Klucz szyfrujacy. Defaults to None.
    """ 
    length=len(string)
    #podział na wiersze
    #generujemy nowe wiersze
    rows=["" for i in range(key)]
        #wpisujemy do listy
    for x in range(length):
     #tutaj ogarnąć wzór na wpisywanie 
        rows[abs((key-1)-abs((key-1)-abs(x%((key-1)*2))))]+=string[x]

    encodedstring=""
    for x in range(key):
        encodedstring+=rows[x]
    return encodedstring
    pass
    #DZIAŁA
def fenceDecipher(string=None, key=None):
    length=len(string)
    indexes=["" for i in range(length)]
    indexes2=[]
    rows=[[] for i in range(key)]

    for x in range(length):
        indexes[x]=((key-1)-abs((key-1)-abs(x%((key-1)*2))))
    #print(indexes)

    for x in range(length):
        rows[indexes[x]].append(x)
    #print(rows)

    for x in range(key):
        indexes2+=rows[x]
    #print(indexes2)

    for x in range(length):
        indexes[(indexes2[x])]=string[x]
    #print(indexes)

    return "".join(str (x) for x in indexes)
    pass


    #DZIAŁĄ:
def columnTransCipher(string=None, key=None):
    """Funkcja szyfrujaca podany ciag znakow za pomoca transpozycji kolumnowej.

    Args:
        string (str, optional): Ciag znakow do szyfrowania. Defaults to None.
        key (int, optional): Klucz szyfrujacy. Defaults to None.
    """
    #Utworzenie wiersza szyfrującego
    seq = [x for x in key],[x for x in range(len(key))]

    for x in range(len(key)):
        for y in range(x,len(key)):
            if seq[0][x]>seq[0][y]:
                #swap podmiana wierszy
                seq[1][x],seq[1][y]=seq[1][y],seq[1][x]

    #podział na wiersze
    rowsnumber=math.ceil(len(string)/len(key))
    matrix= ['' for x in range(len(key))]
    ans= ['' for x in range(len(key))]
    
    for x in range(len(string)):
        matrix[x%len(key)]=''.join((matrix[x%len(key)],string[x]))

    #Dopełnienie wolnych miejsc
    for x in range(len(key)):
        if len(matrix[x])!=rowsnumber:
            matrix[x]= ''.join((matrix[x],random.choice(string.upper())))
    
    #Zamiana kolumn
    for x in range(len(key)):
        ans[seq[1][x]]= matrix[x]
    
    return "".join(str (x) for x in ans)
    pass

    #DZIAŁA
def columnTransDecipher(string=None, key=None):
        #Utworzenie wiersza szyfrującego
    seq = [x for x in key],[x for x in range(len(key))]

    for x in range(len(key)):
        for y in range(x,len(key)):
            if seq[0][x]>seq[0][y]:
                #swap podmiana wierszy
                seq[1][x],seq[1][y]=seq[1][y],seq[1][x]
    
    #podział na wiersze
    rowsnumber=math.ceil(len(string)/len(key))
    matrix= ['' for x in range(len(key))]
    ans= ['' for x in range(len(key))]
    
    for x in range((len(key))):
        matrix[x]=string[x*(rowsnumber):(x+1)*rowsnumber]

    #ustalenie kolejności
    for x in range(len(key)):
        ans[x]= matrix[seq[1][x]]
    #odczyt wierszy
    ansstr=""
    for x in range(len(string)):
        ansstr= ''.join((ansstr,ans[x%len(key)][math.floor(x/len(key))])) 
    return ansstr
    pass

    #TODO:lookForCipher():
def lookForCipher():
    pass

    #TODO:INTERFEJS
if __name__ == "__main__":
    anystring='AlA Ma KoTA       A kot ma \n\n ALE '
    #proste parsowanie
    anystring=anystring.upper() #Tylko wielkie litery
    anystring=anystring.translate({ord(c):None for c in string.whitespace}) #Usuwanie znaków białych i końca linii

    encoded=fenceCipher(anystring,4)
    print(encoded)
    decoded= fenceDecipher(encoded,4)
    print(decoded)
    encoded = columnTransCipher(anystring,'KABANOS')
    print(encoded)
    decoded = columnTransDecipher(encoded,'KABANOS')
    print (decoded)
    pass