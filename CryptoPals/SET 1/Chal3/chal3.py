from Crypto.Util.number import *

chiper = 0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
bchiper = long_to_bytes(chiper)

for j in range(0x00, 0xff):
	 plaint = ""
	 for i in bchiper:
	 	plaint += chr(ord(i) ^ j)
	 print j, plaint

# 88 Cooking MC's like a pound of bacon