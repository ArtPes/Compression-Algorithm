import os, math


def output(lock, message):
    lock.acquire()
    print(message)
    lock.release()


def get_shareable_files():
    files_list = []
    for root, dirs, files in os.walk("files_executed"):
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


def stampa_binario(text, file_path):
    binario = ' '.join(format(x, 'b') for x in bytearray(text, 'utf-8'))

    #l = file_path.split('.')
    #new_path = l[0] + str('_binary.') + l[1]

    testo_binario = open('./files_executed/' + file_path + str('_binary.txt'), 'w')
    for c in binario:
        testo_binario.write(str(c))
    testo_binario.close()
