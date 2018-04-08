from LZW import *
from RLE import *


def start_LZW(text):
    # comprimo il testo
    compressed_LZW = LWZ_compress(text)

    # scrivo su file il testo compresso
    compress_text_LZW = open('compress_text_LZW', 'w')
    for c in compressed_LZW:
        compress_text_LZW.write(str(c))
    compress_text_LZW.close()

    print('Done Compression!')
    # decomprimo il testo
    decompressed_LZW = LWZ_decompress(compressed_LZW)

    # scrivo su file il testo decompresso
    decompress_text_LZW = open('decompress_text_LZW', 'w')
    for d in decompressed_LZW:
        decompress_text_LZW.write(d)
    decompress_text_LZW.close()

    print('Done Decompression!')


def start_RLE(text):
    compressed_RLE = RLE_encode(text)
    # scrivo su file il testo compresso
    compress_text_RLE = open('compress_text_RLE', 'w')
    for c in compressed_RLE:
        compress_text_RLE.write(str(c))
    compress_text_RLE.close()

    print('Done Compression!')
    # decomprimo il testo
    decompressed_RLE = RLE_decode(compressed_RLE)

    # scrivo su file il testo decompresso
    decompress_text_RLE = open('decompress_text_RLE', 'w')
    for d in decompressed_RLE:
        decompress_text_RLE.write(d)
    decompress_text_RLE.close()

    print('Done Decompression!')


def hashfile(file, hasher, blocksize=65536):
    """
    Esegue la funzione di hash sul contenuto del file per ottenere l'md5
    :param file: file su cui effettuare l'hash md5
    :type file: file
    :param hasher: componente che esegue l'hash
    :type hasher: object
    :param blocksize: dimensione del buffer di lettura del file
    :type blocksize: int
    :return: hash md5 del file
    :rtype: str
    """

    buf = file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = file.read(blocksize)
    return hasher.hexdigest()