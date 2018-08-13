#Author: hashs3v3n
#Feel free to modify and use it.

def lookup(indexing_string, char):
	if indexing_string == "":
		indexing_string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	return indexing_string.find(char)

def bit_adjuster(string):
	if len(string) <= 6:
		for x in range(6):
			if len(string) == 6:
				return string
				break
			else:
				string = "0" + string
	else:
		print("Invalid length passed.")
	return string	
		
def main():
	base64_str = raw_input("Enter string to decode: ")
	while True:
                indexing_string = raw_input("Enter the indexing string or simply press enter to use default: ")
                if len(indexing_string) == 64 or len(indexing_string) == 0:
                        break
                else:
                        print("Indexing string length invalid. Please re-enter")

	
	#Converting base64 char into six binary bits
	bin_str = ""
	
	for char in base64_str:
		temp = bin(lookup(indexing_string,char))[2:]
		bin_str += bit_adjuster(temp)
	
	#Decoding the stream of bits
	decoded_str=""
	
	for x in range(0,len(bin_str), 8):
		decoded_str += chr(int(bin_str[x:x+8],2))

	#Removal of padding	
	if decoded_str[-2] == "=":
		decoded_str = decoded_str[:len(decoded_str)-2]
	elif decoded_str[-1] == "=":
		decoded_str = decoded_str[:len(decoded_str)-1]

	print ("The decoded string is :")
	print (decoded_str)
	

main()
