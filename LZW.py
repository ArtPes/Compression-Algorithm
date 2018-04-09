from io import StringIO


def LWZ_compress(uncompressed):
    """Comprime una stringa in una lista di simboli."""

    # costruisco il dizionario
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        #print('stringa: '+wc)
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc al dizionario
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        result.append(dictionary[w])
    return result


def LWZ_decompress(compressed):
    """Decomprime una stringa in una lista di simboli."""
    # analogo alla compressione

    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()

print(r'''
 __       ________  ____    __    ____ 
|  |     |       /  \   \  /  \  /   / 
|  |     `---/  /    \   \/    \/   /  
|  |        /  /      \            /   
|  `----.  /  /----.   \    /\    /    
|_______| /________|    \__/  \__/     

''')

