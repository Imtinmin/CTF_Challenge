enc='reverse+'
dec1=''
table='373435323330313E3F3C3D3A3B383926272425222320212E2F2C171415121310111E1F1C1D1A1B181906070405020300010E0F0C46474445424340414E4F5D59'.decode('hex')
dec2=[]
flag=''

for i in enc:
    dec1+=chr(ord(i)^0x76)
for i in dec1:
    dec2.append(table.index(i))

print dec2

for i in range(int(len(dec2)/4)):
	a = dec2[4*i+0]
	b = dec2[4*i+1]
	c = dec2[4*i+2]
	d = dec2[4*i+3]
	flag += chr(a << 2 | b >> 4)
	flag += chr(b << 2 | c >> 4)
	flag += chr(c << 2 | d >>4 )

print "DDCTF{%s}"%flag.encode("hex").upper()