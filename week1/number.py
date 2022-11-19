"""
Monellako tavalla kokonaisluku n voidaan esittää positiivisten kokonaislukujen summana? Kaksi tapaa ovat erilaiset, jos summat eroavat, kun luvut järjestetään pienimmästä suurimpaan. Summassa voi olla myös vain yksi luku.

Esimerkiksi luku 5 voidaan esittää seuraavilla tavoilla: 5, 1+4, 2+3, 1+1+3, 1+2+2, 1+1+1+2 ja 1+1+1+1+1.

Voit olettaa, että n on välillä 1…50. Koodisi tulee laskea vastaus itse (eli siinä ei saa olla esimerkiksi listaa, jossa on valmiit vastaukset joka testiin).
"""

import copy
 
def apu(n, nykysumma, alku, palauta, tulos):
    if nykysumma == n:
        palauta.append(copy.copy(tulos))
 
    for i in range(alku, n):
        temp_sum = nykysumma + i
        if temp_sum > n:
            return
        tulos.append(i)
        apu(n, temp_sum, i, palauta, tulos)
        tulos.pop()
 
def count(n):
    palauta = []
    result = []
    apu(n, 0, 1, palauta, result)
    return len(palauta)+1
 
if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    print(count(42)) # 53174
