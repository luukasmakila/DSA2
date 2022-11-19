"""
Tehtäväsi on muodostaa lista, jossa on kaikki annetun merkkijonon anagrammit eli kaikki merkkijonot, jotka voidaan muodostaa merkkijonon merkeistä. Listan tulee olla aakkosjärjestyksessä.

Voit olettaa, että merkkijono muodostuu merkeistä a-z ja siinä on enintään 8 merkkiä.
"""

def create(s):

    if len(s) < 2:
        return [s]

    lista = []
    for anagram in create(s[1:]):
        for i in range(len(s)):
            if (anagram[:i] + s[0:1] + anagram[i:]) not in lista:
                lista.append(anagram[:i] + s[0:1] + anagram[i:])
    return sorted(lista)
 
if __name__ == "__main__":
    print(create("b"))
    print(create("ab")) # [ab,ba]
    print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(create("aybabtu"))) # 1260
