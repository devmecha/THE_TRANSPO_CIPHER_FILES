import time, os, sys, transposition_cipher, dec_transposition_cipher
import math
import re

status =''
def validate_status():
	m = input('Please Enter the mode | 0 For Encrypt / 1 for Decrypt')
	if m == '0' :
		st = 'encrypt'
	elif  m == '1' :
		st = 'decrypt'
	else :
			m = input('Invalid Value, again | Type: 0 For Encrypt / Type: 1 for Decrypt')
	return st

def inputFile_status(title):
	if not os.path.lexists(title):
		print('!! The file : %s does not exist. Proccess stops now !' % (title))
		sys.exit()

def outputFile_status(title):
	if os.path.lexists(title):
		print('!! The file : %s already exist.You want to continue ? (Y)es or (N)o ?' %(title))
		response = input('> ')
		if not response.lower().startswith('y'):
			sys.exit()
def readFile(title):
	iFile = open(title)
	iText = iFile.read()
	iFile.close()
	return iText

def writeFile(title, text):
	oFile = open(title, 'w')
	oFile.write(text)
	oFile.close()

def trans_cipher(st, k, text, timer):
	if st == 'encrypt':
		res = transposition_cipher.trans_cipher_enc(text, k )
	elif st == 'decrypt':
		res = dec_transposition_cipher.trans_cipher_dec(text, k )
	t = round(time.time() - timer, 2)
	print('Done in : %s seconds' % t)
	return res

def Main():
	print("****** FILES TRANSPOSITION CIPHER || Encypting & Decrypting *******")
	status = validate_status() # Encypting or Decrypting
	print('\n')
	key = input('Please Enter your Key')
	print('\n')

	inputFile = input('Please Enter your InputFile location  :') #File's location (name)
	print('\n')
	inputFile_status(inputFile) #Check if it exist or not
	print('\n')
		# Output File 
	outputFile = input('Please Enter your OutputFile location  :') #File's location (name)
	print('\n')
	outputFile_status(outputFile) #Check if it exist or not
	print('\n')
		# Read the content of Input File
	text = readFile(inputFile)
		#
	print('-------------All in All------------------')
	print('Mode : %s ' %status )
	print('\n')
	print('The Key is : %s ' %key )
	print('\n')
	print('InputFile : %s ' %inputFile )
	print('\n')
	print('OutputFile : %s ' %outputFile )
	print('\n')
	print('---------------------------------')
	print('\n')
		# Transposition Cipher Processing ...
	print('Processing now ...')
	print('\n')
	timer = time.time()
	result = trans_cipher(status, key, text,timer)
	t = round(time.time() - timer, 2)
		# Write in the output File
	writeFile(outputFile, result )
	print('------------- SUMMARY ---------------------')
	print('Mode : %s ' %status )
	print('\n')
	print('The Key is : %s ' %key )
	print('\n')
	print('InputFile : %s ' %inputFile )
	print('\n')
	print('OutputFile : %s ' %outputFile )
	print('\n')
	print('Process time : %s ' %t )
	print('\n')
	print('-------------------------------------------')
if __name__ == '__main__':
 	Main()