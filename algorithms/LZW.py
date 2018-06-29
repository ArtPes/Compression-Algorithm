from io import StringIO
import time


def LWZ_compress(text):
    # costruisco il dizionario
    dict_size = 127
    dictionary = {chr(i): i for i in range(0, dict_size)}

    # prefisso NULLO
    w = ""
    result = []
    for c in text:
        # prende un carattere e lo somma al precedente
        wc = w + c
        # print('stringa: '+wc)
        if wc in dictionary:  # se è già presente nel dizionario
            w = wc
        else:  # se non è presente nel dizionario
            result.append(dictionary[w])
            # Add wc al dizionario e ne aumento la lunghezza
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        result.append(dictionary[w])
    '''
    for a in dictionary:
        print(a)
    print(len(dictionary))
    '''
    #print("IL DIZIONARIO: " + str(dictionary) + " \nlungo: " + str(len(dictionary)))
    return result


def LWZ_decompress(compressed):
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


def start_LZW(text, file_path):
    T1c = time.time()
    # comprimo il testo
    compressed_LZW = LWZ_compress(text)
    T2c = time.time()
    # scrivo su file il testo compresso
    compress_text_LZW = open('files_executed/' + file_path + '_c_LZW', 'w')
    for c in compressed_LZW:
        compress_text_LZW.write(str(c))
    compress_text_LZW.close()

    print('Done Compression in: %.3f seconds' % (T2c - T1c))

    T1d = time.time()
    # decomprimo il testo
    decompressed_LZW = LWZ_decompress(compressed_LZW)
    T2d = time.time()
    # scrivo su file il testo decompresso
    decompress_text_LZW = open('files_executed/' + file_path + '_d_LZW', 'w')
    for d in decompressed_LZW:
        decompress_text_LZW.write(d)
    decompress_text_LZW.close()

    print('Done Decompression in: %.3f seconds' % (T2d - T1d))

    a = 'files_executed/' + file_path + '_c_LZW'
    b = 'files_executed/' + file_path + '_d_LZW'

    return a, b
