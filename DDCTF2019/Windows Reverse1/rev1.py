s1 = 'F'*32 + 'F'*16 + "FEFFFFFF01000000"
s = s1.decode("hex")+"~}|{zyxwvutsrqponmlkjihgfedcba`_^]\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)(',27h,'&%$#! "

a = "DDCTF{reverseME}"
flag = ''
for i in a:
	flag += chr(s.index(i))

print "DDCTF{%s}"%flag