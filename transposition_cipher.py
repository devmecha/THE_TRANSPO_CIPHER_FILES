import math
import re

def trans_cipher_enc (msg, k):
	matrix = [''] * int(k)
	for c in range(int(k)) :
		position = c
		while position < len(msg) : # 
			matrix[c] += msg[position]
			position += int(k) #next position
	return ''.join(matrix)

def Main():
	print("****** TRANSPOSITION CIPHER || Encryption *******")
	msg = input('Please Enter your Message  :')
	key = input('Please Enter your Key :')
	print('the message is : ', msg)
	print('\n')
	print('The Key is : ', key )
	print('\n')
	print('Processing now ...' )
	res = trans_cipher_enc(msg, key)
	print("Warning ! The '|' at the end is not included")
	print("Encrypted msg is : %s " %(res+'|'))
if __name__ == '__main__':
 	Main()