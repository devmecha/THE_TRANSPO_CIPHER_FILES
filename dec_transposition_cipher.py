import math
import re

def trans_cipher_dec (msg, k):
	l = len(msg)
	# Number of Columns
	nC = int(math.ceil(l/float(k)))
	# Number of Rows
	nR = int(k)
	# Number of empty cases
	nE = (nC * nR) - l
	# Build the matrix
	matrix = [''] * nC
	c = 0 #column
	r = 0 #row
	for z in msg :
		matrix[c] += z
		c += 1 # Next column
		if(c == nC) or (c == nC-1 and r >= nR-nE ): # no more columns or reached empty box
			c =0
			r += 1
	return ''.join(matrix)

def Main():
	print("****** TRANSPOSITION CIPHER || Decrypting *******")
	msg = input('Please Enter your Message  :')
	key = input('Please Enter your Key :')
	print('the message is : ', msg)
	print('\n')
	print('The Key is : ', key )
	print('\n')
	print('Processing now ...' )
	res = trans_cipher_dec(msg, key)
	print("Warning ! The '|' at the end is not included")
	print("Decrypted msg is : %s " %(res+'|'))
if __name__ == '__main__':
 	Main()