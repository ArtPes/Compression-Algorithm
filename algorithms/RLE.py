import time


def RLE_encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        # se il carattere corrente è diverso dal precedente istanzia la tupla
        if character != prev:
            # se c'è un precedente carattere crea la tupla
            if prev:
                entry = prev, count
                lst.append(entry)
                # print lst
            count = 1
            prev = character
        else: # incrementa occorrenze
            count += 1
    try:
        entry = character, count
        lst.append(entry)
        return lst
    except Exception as e:
            print("Exception encountered {e}".format(e=e))
            return e


def RLE_decode(lst):
    q = ""
    # prende ogni carattere nella lista e lo moltiplica per le occorrenze
    for character, count in lst:
        q += character * count
    return q


def start_RLE(text, file_path):
    T1c = time.time()
    compressed_RLE = RLE_encode(text)
    T2c = time.time()
    # scrivo su file il testo compresso
    compress_text_RLE = open('files_executed/' + file_path + '_c_RLE', 'w')
    for c in compressed_RLE:
        compress_text_RLE.write(str(c))
    compress_text_RLE.close()

    print('Done Compression in: %.3f seconds' % (T2c - T1c))

    T1d = time.time()
    # decomprimo il testo
    decompressed_RLE = RLE_decode(compressed_RLE)
    T2d = time.time()
    # scrivo su file il testo decompresso
    decompress_text_RLE = open('files_executed/' + file_path + '_d_RLE', 'w')
    for d in decompressed_RLE:
        decompress_text_RLE.write(d)
    decompress_text_RLE.close()

    print('Done Decompression in: %.3f seconds' % (T2d - T1d))

    b = 'files_executed/' + file_path + '_d_RLE'
    a = 'files_executed/' + file_path + '_c_RLE'
    return a, b
