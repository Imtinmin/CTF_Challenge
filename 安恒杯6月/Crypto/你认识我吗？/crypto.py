from message import plainText
from message import key

pla_len = len(plainText)
key_len = len(key)

print "plainText length is %d" % pla_len
print "key length is %d" % key_len

pla_matrix = []
for i in range(0,pla_len,key_len):
	pla_matrix.append(list(plainText[i:i+key_len]))

ord_key = []
for k in key:
	ord_key.append(ord(k))

ord_key = sorted(ord_key)

output_order = []

for i in ord_key:
	output_order.append(key.find(chr(i)))

for i in output_order:
	for s in pla_matrix:
		print s[i],
	print "\n"