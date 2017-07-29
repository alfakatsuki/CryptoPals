def bagikalimat(kalimat):
	return kalimat.split(' ')

def cocokin(words, kamus):
	if(len(words)<3):
		return 0
	return words in kamus



from Crypto.Util.number import *

dump = open('Chal4.txt', 'r')
rawss = dump.read()


arrchiper = rawss.split('\n')

dump = open('/usr/share/dict/words', 'r')
kams = dump.read()
kams = kams.split('\n')
kams = kams[:-1]
hasil = []
kelar = 0
for p, i in enumerate(arrchiper):
	strdmp = long_to_bytes(eval('0x'+i))
	for j in range(0x00, 0xff):
		appending = 0
		decodes = ""
		for k in strdmp:
			decodes += chr(ord(k) ^ j)
		words = bagikalimat(decodes)
		#print words
		for l in words:
			#print l

			if(cocokin(l, kams)):
				appending = 1
		if(appending):
			print decodes, i, j, p
			hasil.append(decodes)


# After Run For Few Minutes I Got The Right String
# Now that the party is jumping

Answer = """
Now that the party is jumping
7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f 53 170
"""