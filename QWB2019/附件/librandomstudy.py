import random
import time
import subprocess

def bye():
	print "[+]bye~"
	sys.exit()

def challenge1():
	print "[+]Generating challenge 1"
	random.seed(int(time.time()))
	for i in range(200):
		recv=int(raw_input("[-]"))
		if recv==random.randint(0,2**64):
			print "[++++++++++++++++]challenge 1 completed[++++++++++++++++]"
			return
		else:
			print "[+]failed"
	bye()


def challenge2():
	print "[+]Generating challenge 2"
	for i in range(200):
		o = subprocess.check_output(["java", "Main"])
		tmp=[]
		for i in o.split("\n")[0:3]:
		    tmp.append(int(i.strip()))
		v1=tmp[0] % 0xffffffff
		v2=tmp[1] % 0xffffffff
		v3=tmp[2] % 0xffffffff
		print "[-]"+str(v1)
		print "[-]"+str(v2)
		v3_get=int(raw_input("[-]"))
		if v3_get==v3:
			print "[++++++++++++++++]challenge 2 completed[++++++++++++++++]"
			return
		else:
			print "[+]failed"
	bye()

def challenge3():
	print "[+]Generating challenge 3"
	for i in range(1000):
	    a=raw_input("[-]")
	    target=random.getrandbits(32)
	    if a!=str(target):
	        print "[+]failed:"+str(target)
	    else:
			print "[++++++++++++++++]challenge 3 completed[++++++++++++++++]"
			return
	bye()