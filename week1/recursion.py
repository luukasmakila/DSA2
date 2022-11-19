import time
 
def rekursio(n):
    if n <= 2:
        return n
    return rekursio(n-1) + rekursio(n-2) + rekursio(n-3)
 
if __name__ == "__main__":
    alku = time.time()
    print(rekursio(30))
    loppu = time.time()
    print(loppu-alku)
