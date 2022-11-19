"""
Annettuna on lista kokonaislukuja ja tehtäväsi on selvittää, onko luvut mahdollista jakaa kahteen ryhmään niin, että molempien ryhmien summa on sama.

Esimerkiksi kun lista on [9,4,8,7,6], mahdollinen ratkaisu on muodostaa ryhmät [8,9] ja [4,6,7]. Tällöin kummankin ryhmän lukujen summa on 17.

Voit olettaa, että jokainen luku on välillä 1…109 ja että listalla on enintään 16 lukua.
"""

def check(t):
 
    if sum(t) % 2 == 1:
        return False

    setti = set()
    setti.add(0)
    kohde = sum(t) // 2
 
    for i in range(len(t) - 1, -1, -1):
        seuraavaSetti = set()
        for j in setti:
            if j + t[i] == kohde:
                return True
            seuraavaSetti.add(j + t[i])
            seuraavaSetti.add(j)
        setti = seuraavaSetti

    if kohde in setti:
        return True
    return False

if __name__ == "__main__":
    print(check([3,4,5])) # False
    print(check([16,8,4,4])) # True
    print(check([9,4,8,7,6])) # True
    print(check([1,2,3,4,5,6])) # False
    print(check([1,2,3,4,5,6,7])) # True
    print(check([4,4,4,6,6])) # True
