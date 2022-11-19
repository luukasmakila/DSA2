"""
Tehtäväsi on muodostaa lista, jossa on kaikki n merkin pituiset merkkijonot, joissa jokainen merkki on A, B tai C. Listan tulee olla aakkosjärjestyksessä.

Voit olettaa, että n on välillä 1…10.
"""

def create(k):

    kirjaimet = ["A", "B", "C"]
    n = len(kirjaimet)
    lista = []
    apu(kirjaimet, "", n, k, lista)
    return lista
 
def apu(kirjaimet, pref, n, k, lista:list):

    if k == 0:
        lista.append(pref)
        return

    for i in range(n):
        newPref = pref + kirjaimet[i]
 
        apu(kirjaimet, newPref, n, k-1, lista)
 
if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AA,AB,AC,BA,BB,BC,CA,CB,CC] 
    print(len(create(5))) # 243
