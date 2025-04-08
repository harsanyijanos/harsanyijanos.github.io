import os
cwd = os.getcwd()
fileFolder = cwd + '\\AlapVizsga\\2025\\tmp\\'

with open(fileFolder+'konyvek-adatok.txt', 'r', encoding='utf-8') as fr:
    with open(fileFolder+'konyvek.txt', 'w', encoding='utf-8') as fw:
        for line in fr:
            item = line.replace('\n','').split(';')
            usor = item[0]+';'+item[1]+';'+item[4]+'\n'
            fw.write(usor)
        '''
        sor = fr.readline()
        item = sor.split(';')
        usor = item[0]+';'+item[1]+';'+item[4]+'\n'
        fw.write(usor)
        '''

