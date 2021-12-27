

#本程序实现对Unicode字符串进行编码和解码

a = input('请输入要加密的字符串\n')

for i in a:
	print(chr(ord(i) + 3),end = '')   #每个字符加3
	
print('\n')	

#解码
a_decode = input('请输入要解码的字符串\n')
for i in a_decode:
	print(chr(ord(i) - 3),end = '')   #每个字符加3
