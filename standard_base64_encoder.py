#Author: Hashs3v3n
#Feel free to modify and use it

def lookup(index):
	indexing_string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	return indexing_string[index]

def bit_adjuster(string):
	if len(string) <= 8:
		for x in range(8):
			if len(string) == 8:
				return string
				break
			else:
				string = "0" + string
	else:
		print("Invalid length passed.")
	print(string)
	return string	
		
def main():
	input_str = raw_input("Enter string to encode: ")
	pad = "="
	if len(input_str) % 3 == 1:
		input_str = input_str + pad + pad
	elif len(input_str) % 3 == 2:
		input_str = input_str + pad 
	print (input_str)
	bin_str = ""
	
	for x in input_str:
		temp = bin(ord(x))[2:]
		bin_str += bit_adjuster(temp)
	
	base64_str=""
	
	for x in range(0,len(bin_str), 6):
		base64_str += lookup(int(bin_str[x:x+6],2))
	print("The original string is :" + input_str)
	print ("Base64 encoded string is :")
	print (base64_str)
	

main()
