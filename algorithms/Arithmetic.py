import sys
import random
import string

import decimal
from decimal import Decimal

decimal.getcontext().prec = 25


def encode(encode_str, N):
    asciiDict = {chr(i) for i in range(129)}
    num_let = len(asciiDict)
    count = dict.fromkeys(asciiDict, 1)     # probability table
    cdf_range = dict.fromkeys(asciiDict, 0)
    pdf = dict.fromkeys(asciiDict, 0)


    low = 0
    high = Decimal(1) / Decimal(num_let)

    for key, value in sorted(cdf_range.items()):
        cdf_range[key] = [low, high]
        low = high
        high += Decimal(1) / Decimal(num_let)

    for key, value in sorted(pdf.items()):
        pdf[key] = Decimal(1) / Decimal(num_let)

    # for key, value in sorted(cdf_range.items()):
    #   print key, value

    # for key, value in sorted(pdf.items()):
    #   print key, value

    i = num_let

    lower_bound = 0  # upper bound
    upper_bound = 1  # lower bound

    u = 0

    # go thru every symbol in the string
    for sym in encode_str:
        i += 1
        u += 1
        count[sym] += 1

        curr_range = upper_bound - lower_bound  # current range
        upper_bound = lower_bound + (curr_range * cdf_range[sym][1])  # upper_bound
        lower_bound = lower_bound + (curr_range * cdf_range[sym][0])  # lower bound

        # update cdf_range after N symbols have been read
        if (u == N):
            u = 0

            for key, value in sorted(pdf.items()):
                pdf[key] = Decimal(count[key]) / Decimal(i)

            low = 0
            for key, value in sorted(cdf_range.items()):
                high = pdf[key] + low
                cdf_range[key] = [low, high]
                low = high
    print(lower_bound)
    return lower_bound


def decode(encoded, strlen, every):
    decoded_str = ""

    asciiDict = {chr(i) for i in range(129)}
    num_let = len(asciiDict)
    count = dict.fromkeys(asciiDict, 1)     # probability table
    cdf_range = dict.fromkeys(asciiDict, 0)
    pdf = dict.fromkeys(asciiDict, 0)

    low = 0
    high = Decimal(1) / Decimal(num_let)

    for key, value in sorted(cdf_range.items()):
        cdf_range[key] = [low, high]
        low = high
        high += Decimal(1) / Decimal(num_let)

    for key, value in sorted(pdf.items()):
        pdf[key] = Decimal(1) / Decimal(num_let)

    lower_bound = 0  # upper bound
    upper_bound = 1  # lower bound

    k = 0

    while (strlen != len(decoded_str)):
        for key, value in sorted(pdf.items()):

            curr_range = upper_bound - lower_bound  # current range
            upper_cand = lower_bound + (curr_range * cdf_range[key][1])  # upper_bound
            lower_cand = lower_bound + (curr_range * cdf_range[key][0])  # lower bound

            if (lower_cand <= encoded < upper_cand):
                k += 1
                decoded_str += key

                if (strlen == len(decoded_str)):
                    break

                upper_bound = upper_cand
                lower_bound = lower_cand

                count[key] += 1

                if (k == every):
                    k = 0
                    for key, value in sorted(pdf.items()):
                        pdf[key] = Decimal(count[key]) / Decimal(num_let + len(decoded_str))

                    low = 0
                    for key, value in sorted(cdf_range.items()):
                        high = pdf[key] + low
                        cdf_range[key] = [low, high]
                        low = high

    print(decoded_str)


def main():
    count = 10
    encode_str = "ciao!!123"
    strlen = len(encode_str)
    every = 1
    encoded = encode(encode_str, every)
    decoded = decode(encoded, strlen, every)


if __name__ == '__main__':
    main()


    T1c = time.time()

    # comprimo il testo
    for s in text.split():
        encoded = encode(s.lower(), probabilities)
        # decoded = decode(encoded, probabilities)
        lista_enc.append(encoded)
    T2c = time.time()

    # scrivo su file il testo compresso
    compress_text_ARITHM = open('files_executed/' + file_path + '_c_ARITHM', 'w')
    for c in lista_enc:
        compress_text_ARITHM.write(str(c) + ' ')
    compress_text_ARITHM.close()

    print('Done Compression in: %.3f seconds' % (T2c - T1c))

    T1d = time.time()
    # decomprimo il testo
    for l in lista_enc:
        decoded = decode(l, probabilities)
        lista_dec.append(decoded)
    T2d = time.time()
    # scrivo su file il testo decompresso
    decompress_text_ARITHM = open('files_executed/' + file_path + '_d_ARITHM', 'w')
    for d in lista_dec:
        decompress_text_ARITHM.write(str(d) + ' ')
    decompress_text_ARITHM.close()

    print('Done Decompression in: %.3f seconds' % (T2d - T1d))

    a = 'files_executed/' + file_path + '_c_ARITHM'
    b = 'files_executed/' + file_path + '_d_ARITHM'

    return a, b
