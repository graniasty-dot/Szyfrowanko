import tkinter
import cmath
    #DZIAŁA ZROBIONE SZYFROWANIE
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
    print(rows)
    for x in range(length):
     #tutaj ogarnąć wzór na wpisywanie 
        rows[abs((key-1)-abs((key-1)-abs(x%((key-1)*2))))]+=string[x]

    print(rows)
    encodedstring=""
    for x in range(key):
        encodedstring+=rows[x]
    return encodedstring
    pass
#w trakcie prac
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

def columnTransCipher(string=None, key=None):
    """Funkcja szyfrujaca podany ciag znakow za pomoca transpozycji kolumnowej.

    Args:
        string (str, optional): Ciag znakow do szyfrowania. Defaults to None.
        key (int, optional): Klucz szyfrujacy. Defaults to None.
    """
    pass

def columnTransDecipher():
    pass

def lookForCipher():
    pass


if __name__ == "__main__":

    encoded=fenceCipher('ALAMAKOTAAKOTMAALE',4)
    print(encoded)
    decoded= fenceDecipher(encoded,4)
    print(decoded)
    pass