import re
import base64
v5 = 90
v6 = 109
v7 = 120
v8 = 104
v9 = 90
v10 = 51
v11 = 116
v12 = 116
v13 = 89
v14 = 87
v15 = 90
v16 = 104
v17 = 97
v18 = 51
v19 = 86
v20 = 104
v21 = 97
v22 = 87
v23 = 120
v24 = 104
v25 = 97
v26 = 88
v27 = 70
v28 = 112
v29 = 89
v30 = 87
v31 = 53
v32 = 107
v33 = 89
v34 = 87
v35 = 57
v36 = 105
v37 = 102
v38 = 81
v39 = 61
v40 = 61
f = open('1.py','r').read()
vl = re.findall('= .*?(.*?)\n',f)
print "".join(chr(int(i)) for i in vl[:-2])
print base64.b64decode("".join(chr(int(i)) for i in vl[:-2]))

