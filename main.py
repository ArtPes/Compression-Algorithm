from helper import *
import hashlib
import time

# apro il file da comprimere
file_path = r"lotr.txt"
with open(file_path,'r') as f:
    text = f.read()


md5_original = hashfile(open(file_path, 'rb'), hashlib.md5())
print('File size is: '+str(file_size(file_path)))
print('It is md5 is: '+ str(md5_original))
#####################################################################
print(r'''
    ___       ___       ___   
   /\__\     /\  \     /\__\  
  /:/  /    _\:\  \   /:/\__\ 
 /:/__/    /::::\__\ /:/:/\__\
 \:\  \    \::;;/__/ \::/:/  /
  \:\__\    \:\__\    \::/  / 
   \/__/     \/__/     \/__/  
''')
# START LZW
start_LZW(text)
file_path1 = r"files/compress_text_LZW"
file_path2 = r"files/decompress_text_LZW"
md5_LZW = hashfile(open(file_path2, 'rb'), hashlib.md5())

if md5_LZW == md5_original:
    print('File is intact, md5 is: '+str(md5_LZW))
######################################################################
print(r'''
    ___       ___       ___   
   /\  \     /\__\     /\  \  
  /::\  \   /:/  /    /::\  \ 
 /::\:\__\ /:/__/    /::\:\__\
 \;:::/  / \:\  \    \:\:\/  /
  |:\/__/   \:\__\    \:\/  / 
   \|__|     \/__/     \/__/  
''')
# start RLE
start_RLE(text)
file_path3 = r"files/compress_text_RLE"
file_path4 = r"files/decompress_text_RLE"
print('Compress: '+str(file_size(file_path3))+' bytes')
md5_RLE = hashfile(open(file_path4, 'rb'), hashlib.md5())

if md5_LZW == md5_original:
    print('File is intact, md5 is: '+str(md5_LZW))
######################################################################