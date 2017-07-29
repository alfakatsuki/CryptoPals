from Crypto.Util.number import *

def encrepeat(sentences, key):

	chiper = ""
	for i in key:
		
		chiper = ""
		for j in sentences:

			charr = chr(ord(j) ^ ord(i))

			chiper += charr
		sentences = chiper
	return hex(bytes_to_long(chiper))


plaint = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

plaint = plaint.split('\n')

key = "ICE"

for i in plaint:
	print i
	print i, encrepeat(i, key)
