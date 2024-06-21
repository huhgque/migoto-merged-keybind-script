#!/usr/bin/python

import os

def main():
    ini_file_check = ["merged.ini","Firefly.ini"]
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk("."):
        path = root.split(os.sep)
        # print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            for ini_name in ini_file_check:
                if file.__contains__(ini_name) :
                    result = ini_write(root+"\\"+file)
                    if result == 1 :
                        print("Done "+root)
                    else :
                        print("Fail "+root)


def ini_write(path):
    f = open(path,"r")
    controll_key = ["alt","ctrl"]
    controll_key_index = 0
    current_controll_key_use = controll_key[controll_key_index]
    counter = 1
    lines = []
    for line in f:
        if line.__contains__("key = "):
            lines.append( "key = "+current_controll_key_use+" "+counter.__str__()+"\n")
            counter+=1
            if counter > 9:
                counter = 1
                controll_key_index += 1
                current_controll_key_use += " "+controll_key[controll_key_index]
        else :
            lines.append(line)
    f.close()
    f = open(path,"w")
    for line in lines:
        f.write(line)
    return 1
main()