from algorithms.Arithmetic import *
from algorithms.LZW import *
from algorithms.RLE import *
from helper import *
import hashlib, threading, sys

out_lck = threading.Lock()

while True:
    '''
    output(out_lck, "Select one of the following options ('e' to exit): ")
    files_list = get_shareable_files()
    for idx, file in enumerate(files_list):
        output(out_lck, str(idx) + ": " + file)

    int_option = None
    dentro = False
    
    while int_option is None:
        try:
            option = input()
            for idx, file in enumerate(files_list):  # Ricerca del file selezionato
                if idx == option:
                    found = True
                    output(out_lck, "Adding file " + file)
            # apro il file da comprimere
            file_path = './files/'+file
            with open(file_path, 'r') as f:
                text_old = f.read()
            text = text_old[3:]
        except SyntaxError:
            option = None
    
        if option is None:
            output(out_lck, "Please select an option")
        elif option == 'e':
            output(out_lck, "Bye bye")
            sys.exit()          # Interrompo l'esecuzione
        else:
            try:
                int_option = int(option)
            except ValueError:
                print("A number is required")
   
        dentro = True
         '''
    #creo lista files
    files_list = get_shareable_files()
    for idx, file in enumerate(files_list):
        output(out_lck, str(idx) + ": " + file)

    option = input()
    for idx, file in enumerate(files_list):  # Ricerca del file selezionato
        if idx == int(option):
            found = True
            output(out_lck, "Adding file " + file)
            # apro il file da comprimere
            file_path = './files_executed/' + file


    #file_path = './files_executed/lotr_c_LZW'
    with open(file_path, 'r') as f:
        text_old = f.read()
    text = text_old#[3:]
    dentro = True
    # prendo solo nome file
    nf= file_path.split('/')
    new_file_path = nf[2].split('.')[0]
    while dentro :
            output(out_lck, "\nSelect one of the following options ('e' to exit): ")
            output(out_lck, "0: RLE ")
            output(out_lck, "1: LZW ")
            output(out_lck, "2: Aritmetic Compression ")
            output(out_lck, "3: Binario ")
            output(out_lck, "4: Exit ")

            int_option = None
            while int_option is None:
                try:
                    option = input()    # Input da tastiera
                except SyntaxError:
                    option = None

                if option is None:
                    output(out_lck, "Please select an option")
                else:
                    try:
                        int_option = int(option)
                    except ValueError:
                        output(out_lck, "A number is required")
            if int_option == 0:
                md5_original = hashfile(open(file_path, 'rb'), hashlib.md5())
                print('File size is: ' + str(file_size(file_path)))
                print('It is md5 is: ' + str(md5_original))
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
                file_path3, file_path4 = start_RLE(text, new_file_path)
                #file_path3 = r"files_executed/compress_text_RLE"
                #file_path4 = r"files_executed/decompress_text_RLE"
                print('Compress: ' + str(file_size(file_path3)) + ' bytes')
                md5_RLE = hashfile(open(file_path4, 'rb'), hashlib.md5())

                if md5_RLE == md5_original:
                    print('File is intact, md5 is: ' + str(md5_RLE))
                ######################################################################
                dentro = False
            elif int_option == 1:
                md5_original = hashfile(open(file_path, 'rb'), hashlib.md5())
                print('File size is: ' + str(file_size(file_path)))
                print('It is md5 is: ' + str(md5_original))
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
                file_path1, file_path2 = start_LZW(text, new_file_path)
                #file_path1 = r"files_executed/compress_text_LZW"
                #file_path2 = r"files_executed/decompress_text_LZW"
                print('Compress: ' + str(file_size(file_path1)) + ' bytes')
                md5_LZW = hashfile(open(file_path2, 'rb'), hashlib.md5())

                if md5_LZW == md5_original:
                    print('File is intact, md5 is: ' + str(md5_LZW))

                dentro = False
            elif int_option == 2:
                md5_original = hashfile(open(file_path, 'rb'), hashlib.md5())
                print('File size is: ' + str(file_size(file_path)))
                print('It is md5 is: ' + str(md5_original))
                ######################################################################
                Arithmetic(text)
                '''file_path5, file_path6 = start_Aritm(text, new_file_path)
                #file_path5 = r"files_executed/"+new_file_path+"c_Aritm"
                #file_path6 = r"files_executed/d_Aritm"
                print('Compress: ' + str(file_size(file_path5)) + ' bytes')
                md5_Aritm = hashfile(open(file_path6, 'rb'), hashlib.md5())

                if md5_Aritm == md5_original:
                    print('File is intact, md5 is: ' + str(md5_Aritm))
                else:
                    print('File IS NOT intact, md5 is: ' + str(md5_Aritm))
                '''
                dentro = False
            elif int_option == 3:
                stampa_binario(text, file_path)
                dentro = False
            elif int_option == 4:
                dentro = False
                sys.exit()          # Interrompo l'esecuzione
            else:
                print('Option ' + str(int_option) + ' not available')