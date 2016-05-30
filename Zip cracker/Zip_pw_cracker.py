import zipfile
import optparse
from threading import Thread
import os
import datetime

def crackZipfile(zFile,word):
    try:
        byte_pw = bytes(word,'utf-8')
        zFile.extractall(pwd=byte_pw)
        print('\n[+] Found password: ' + word)
    except:
        pass
    
def main():
    os.system('cls')
    print('\t\t############################################')
    print('\t\t## Zip file password cracker <2015.12.30> ##')
    print('\t\t############################################')
    print('\n\n\n')
    parser = optparse.OptionParser(" Usage:\n\t-f <zipfile> \n\t-p <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-p', dest='dname', type='string', help='specify txt file')
    (options,args) = parser.parse_args()
   
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
      
    else:
        zname = options.zname
        dname = options.dname
      
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    for line in passFile.readlines():
        word = line.strip('\n')
        crackZipfile(zFile,word)
      
if __name__ == '__main__':
    main()
