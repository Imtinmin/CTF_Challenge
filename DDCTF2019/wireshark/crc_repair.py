import binascii
import struct

misc = open('upload.png','rb').read()

# misc[16:20] width
for i in range(1024):
	data = misc[12:20]+struct.pack('>i',i)+misc[24:29]
	crc = binascii.crc32(data) & 0xffffffff
	if crc == struct.unpack('>i',misc[29:33])[0]:
		print i
		print struct.pack('>i',i)
		data = misc[0:20]+struct.pack('>i',i)+misc[24:]
		open('upload_repair.png','wb').write(data)
		break