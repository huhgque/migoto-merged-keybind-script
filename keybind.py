#!/usr/bin/python

import os

def main():
    exclude_file = ["RabbitFX.ini"]
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk("."):
        path = root.split(os.sep)
        # print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            if exclude_file.__contains__(file):
                continue
            if file.__contains__(".ini") and not file.__contains__("DISABLED"):
                print(file)
                result = ini_write(root+"\\"+file)
                if result == 1 :
                    print("Done "+root)
                else :
                    print("Fail "+root)
    print("Press any to quit")
    wait = input()


def ini_write(path):
    f = open(path,"r")
    controll_key = ["alt","ctrl"]
    counter = 1
    cycle = 0
    lines = []
    control_1 = controll_key[0]
    control_2 = "no_" + controll_key[1]
    for line in f:
        if line.__contains__("key = "):
            key_command = "{} {} {}\n"
            lines.append( "key = "+key_command.format(control_1,control_2,counter))
            counter+=1
            if counter > 9:
                counter = 1
                control_2 = controll_key[1]
        else :
            lines.append(line)
    f.close()
    f = open(path,"w")
    for line in lines:
        f.write(line)
    return 1
main()