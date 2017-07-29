from Crypto.Util.number import *

plaint = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""



key = "ICE"
numa = 0
hasil = ""
numa = numa
for bytess in plaint:
	if(numa==3):
		numa=0
	hasil += chr(ord(bytess) ^ ord(key[numa]))
	numa += 1
print plaint
print hex(bytes_to_long(hasil))