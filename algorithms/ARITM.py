from collections import Counter


def cumulative_freq(freq):
    cf = {}
    total = 0
    for b in range(256):
        if b in freq:
            cf[b] = total
            total += freq[b]
    return cf


def arithmethic_coding(bytes, radix):
    # The frequency characters
    freq = Counter(bytes)

    # The cumulative frequency table
    cf = cumulative_freq(freq)

    # Base
    base = len(bytes)

    # Lower bound
    lower = 0

    # Product of all frequencies
    pf = 1

    # Each term is multiplied by the product of the
    # frequencies of all previously occurring symbols
    for b in bytes:
        lower = lower * base + cf[b] * pf
        pf *= freq[b]

    # Upper bound
    upper = lower + pf

    pow = 0
    while True:
        pf //= radix
        if pf == 0: break
        pow += 1

    enc = (upper - 1) // radix ** pow
    return enc, pow, freq


def arithmethic_decoding(enc, radix, pow, freq):
    # Multiply enc by radix^pow
    enc *= radix ** pow

    # Base
    base = sum(freq.values())

    # Create the cumulative frequency table
    cf = cumulative_freq(freq)

    # Create the dictionary
    dict = {}
    for k, v in cf.items():
        dict[v] = k

    # Fill the gaps in the dictionary
    lchar = None
    for i in range(base):
        if i in dict:
            lchar = dict[i]
        elif lchar is not None:
            dict[i] = lchar

    # Decode the input number
    decoded = bytearray()
    for i in range(base - 1, -1, -1):
        pow = base ** i
        div = enc // pow

        c = dict[div]
        fv = freq[c]
        cv = cf[c]

        rem = (enc - pow * cv) // fv

        enc = rem
        decoded.append(c)

    # Return the decoded output
    return bytes(decoded)

'''
radix = 10  # can be any integer greater or equal with 2

for str in b'DABDDB DABDDBBDDBA ABRACADABRA TOBEORNOTTOBEORTOBEORNOT'.split():
    enc, pow, freq = arithmethic_coding(str, radix)
    dec = arithmethic_decoding(enc, radix, pow, freq)

    print("%-25s=> %19s * %d^%s" % (str, enc, radix, pow))


    if str != dec:
        raise Exception("\tHowever that is incorrect!")
'''

def start_Aritm(text, file_path):
    list_enc = []
    list_dec = []
    radix = 10  # can be any integer greater or equal with 2

    for a in text:
        str = bytearray(a, encoding='utf-8')
        enc, pow, freq = arithmethic_coding(str, radix)
        dec = arithmethic_decoding(enc, radix, pow, freq)
        list_enc.append(enc)
        list_dec.append(dec)

    # scrivo il file compresso
    '''compress_text_Aritm = open('files_executed/' + file_path + '_c_Aritm', 'w')
    for l in list_enc:
        compress_text_Aritm.write()
    compress_text_Aritm.close()
    '''
    # scrivo file decompresso
    decompress_text_Aritm = open('files_executed/' + file_path + '_d_Aritm', 'w')
    for l in list_dec:
        decompress_text_Aritm.write(l.decode("utf-8"))
    decompress_text_Aritm.close()


    '''
    compress_text_Aritm = open('files_executed/compress_text_Aritm', 'w')

    for c in enc:
        compress_text_Aritm.write(str(c))
    compress_text_Aritm.close()

    dec = arithmethic_decoding(enc, radix, pow, freq)
    print(dec)
    '''

    a = 'files_executed/'+file_path+'_c_Aritm'
    b = 'files_executed/'+file_path+'_d_Aritm'
    return a, b