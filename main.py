from helper import *
import os
import hashlib
import math


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

with open('lotr.txt','r') as f:
    text = f.read()


md5_original = hashfile(open('lotr.txt', 'rb'), hashlib.md5())
file_path = r"lotr.txt"
print('File size is: '+str(file_size(file_path)))
print('It is md5 is: '+ str(md5_original))

# START LZW
start_LZW(text)

file_path1 = r"files/compress_text_LZW"
file_path2 = r"files/decompress_text_LZW"
print('Compress: '+str(file_size(file_path1)))
md5_LZW = hashfile(open(file_path2, 'rb'), hashlib.md5())

if md5_LZW == md5_original:
    print('File is intact, md5 is: '+str(md5_LZW))

# start RLE
start_RLE(text)

file_path3 = r"files/compress_text_RLE"
file_path4 = r"files/decompress_text_RLE"
print('Compress: '+str(file_size(file_path3))+' bytes')
md5_RLE = hashfile(open(file_path4, 'rb'), hashlib.md5())

if md5_LZW == md5_original:
    print('File is intact, md5 is: '+str(md5_LZW))