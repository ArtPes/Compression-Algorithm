import collections
from decimal import Decimal
# crea dizionario frequenze
def filecharcount(openfile):
    return sorted(collections.Counter(c for l in openfile for c in l).items())


def probabilita():

    file = open ("files_executed/lotr.txt")

    array = filecharcount(file)
    lista_tuple = []

    tot = 0
    for (a,n) in array:
        tot = n + tot

    for (item,freq) in array:
        lista_tuple.append((item, freq/tot))


    probabilities = {}
    #probabilities.update({"#": (Decimal(0.00), Decimal(0.01))})
    low = 0.01
    for (a,b) in lista_tuple:
        high = low + b
        word = {a: (Decimal(low), Decimal(high))}
        probabilities.update(word)
        low = high


    return probabilities

