import os
import random
cwd = os.getcwd()
fileFolder = cwd + '\\AlapVizsga\\2025\\tmp\\'

with open(fileFolder+'konyvek-adatok.txt', 'r', encoding='utf-8') as fr:
    with open(fileFolder+'konyvek.txt', 'w', encoding='utf-8') as fw:
        for line in fr:
            item = line.replace('\n','').split(';')
            usor = item[0]+';'+item[1]+';'+item[4]+';'+str(random.randint(1,15))+'\n'
            fw.write(usor)

