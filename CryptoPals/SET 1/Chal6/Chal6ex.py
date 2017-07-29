from base64 import *
from time import *

def repeatxor(kalimat ,key):
	iters = 0
	akhir = ""
	for i in kalimat:
		akhir += chr(ord(i) ^ ord(key[iters]))
		iters += 1
		if(iters==3):
			iters=0
	return akhir

def breakxor(kalimat):
	akhir = ""
	for j in range(0x00, 0xff):
		for i in kalimat:
			akhir += ord(i) ^ j
		akhir += '\n'

	return akhir


def hamdis(x, y):
	ham = sum([bin(ord(x[i]) ^ ord(y[i])).count('1') for i in range(len(x))])
	return ham/len(x)

dump = open('/usr/share/dict/words', 'r')
kams = dump.read()

kams = kams.split('\n')
kams = kams[:-1]
total=0
ran=0
for j in range(len(kams)):
	for i in range(len(kams)):
		if(len(kams[j])!=4):
			continue
		if(len(kams[j])!=len(kams[i])):
			continue
		ran += 1
		print kams[j], kams[i],
		total += hamdis(kams[j], kams[i])
		print hamdis(kams[j], kams[i]), '\t\t\t\t\t\t', total/ran

