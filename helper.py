from LZW import *
from RLE import *
import os, math, time

def start_LZW(text):
    T1c = time.time()
    # comprimo il testo
    compressed_LZW = LWZ_compress(text)
    T2c = time.time()
    # scrivo su file il testo compresso
    compress_text_LZW = open('files_executed/compress_text_LZW', 'w')
    for c in compressed_LZW:
        compress_text_LZW.write(str(c))
    compress_text_LZW.close()

    print('Done Compression in: %.3f seconds' % (T2c - T1c))

    T1d = time.time()
    # decomprimo il testo
    decompressed_LZW = LWZ_decompress(compressed_LZW)
    T2d = time.time()
    # scrivo su file il testo decompresso
    decompress_text_LZW = open('files_executed/decompress_text_LZW', 'w')
    for d in decompressed_LZW:
        decompress_text_LZW.write(d)
    decompress_text_LZW.close()

    print('Done Decompression in: %.3f seconds'%(T2d - T1d))


def start_RLE(text):
    T1c = time.time()
    compressed_RLE = RLE_encode(text)
    T2c = time.time()
    # scrivo su file il testo compresso
    compress_text_RLE = open('files_executed/compress_text_RLE', 'w')
    for c in compressed_RLE:
        compress_text_RLE.write(str(c))
    compress_text_RLE.close()

    print('Done Compression in: %.3f seconds' %(T2c - T1c))

    T1d = time.time()
    # decomprimo il testo
    decompressed_RLE = RLE_decode(compressed_RLE)
    T2d = time.time()
    # scrivo su file il testo decompresso
    decompress_text_RLE = open('files_executed/decompress_text_RLE', 'w')
    for d in decompressed_RLE:
        decompress_text_RLE.write(d)
    decompress_text_RLE.close()

    print('Done Decompression in: %.3f seconds'%(T2d - T1d))

def output(lock, message):
    lock.acquire()
    print(message)
    lock.release()

def get_shareable_files():
    files_list = []
    for root, dirs, files in os.walk("files"):
        for file in files:
            files_list.append(file)

    return files_list

def hashfile(file, hasher, blocksize=65536):

    buf = file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = file.read(blocksize)
    return hasher.hexdigest()

def file_size(fname):
    statinfo = os.stat(fname)
    return convert_size(statinfo.st_size)

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def stampa_binario(text,file_path):
    binario = ' '.join(format(x, 'b') for x in bytearray(text, 'utf-8'))

    l = file_path.split('.')
    new_path= l[0]+str('_binary.')+l[1]

    testo_binario = open('./files/'+new_path, 'w')
    for c in binario:
        testo_binario.write(str(c))
    testo_binario.close()