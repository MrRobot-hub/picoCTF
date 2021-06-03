#!/usr/bin/env python3 

def split(password):
	return[char for char in password]

inp = input("enter password")
passlst = ""
inp1 = split(inp)
print(inp1)
for chars in inp1:
	print(type(chars))
	passlst.join(ord(chars))
print("pass: ", passlst)
#pass1 = pass_list.split(',')
if passlst == 122100:
	print("welcome")
else:
	print("sorry")
