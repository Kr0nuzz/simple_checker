import os
import requests
from time import sleep
import sys

def banner():
	print ("""\033[1;32;40m  _________.___   _____ __________.____     ___________ _________   ___ _______________________  ____  __._____________________ """)
	sleep(0.1)
	print (""" /   _____/|   | /     \\______    \    |    \_   _____/ \_   ___ \ /   |   \_   _____/\_   ___ \|    |/ _|\_   _____/\______   \ """)
	sleep(0.1)
	print (""" \_____  \ |   |/  \ /  \|     ___/    |     |    __)_  /    \  \//    ~    \    __)_ /    \  \/|      <   |    __)_  |       _/ """)
	sleep(0.1)
	print (""" /        \|   /    Y    \    |   |    |___  |        \ \     \___\    Y    /        \\      \___|    |  \  |        \ |    |   \ """)
	sleep(0.1)
	print ("""/_______  /|___\____|__  /____|   |_______ \/_______  /  \______  /\___|_  /_______  / \______  /____|__ \/_______  / |____|_  / """)
	sleep(0.1)
	print ("""        \/             \/                 \/        \/          \/       \/        \/         \/        \/        \/         \/ """)
	print ("")
	sleep (0.1)
	print (""" simple tool for check website status code """)
	sleep (0.1)
	print (""" author: Kr0nuzz """)
	print ("")
	print ("""[1] simple check
[2] auto add http protocol
[3] mass check \033[1;30;40m""")

def main():
	su = (int(input(""">>""")))
	print (su)
	if su == 1:
		os.system('clear')
		p = input('url >>')
		q = requests.get(p)
		if q.status_code == 200:
			print('ACTIVE')
		else:
			print('DEAD')
	elif su == 2:
		with open('hasill.txt','w') as tulis, open('target.txt','r') as baca:
			bajingan = baca.read().splitlines()
			for i in bajingan:
				tulis.write('https://'+i+'\n')
			os.system('mv hasill.txt target.txt')
		p = input("type to show menu")
		os.system('clear')
	elif su == 3:
		os.system('clear')
		with open('target.txt','r') as f:
			mylist = f.read().splitlines()
			for i in mylist:
				try:
					re = requests.get(i)
					if re.status_code == 200:
						with open('live.txt','a') as live:
							live.write(str(i)+'\n')
						print ("\033[1;34;40m"+str(i)+"\033[1;30;40m"+" == "+"\033[1;32;40m LIVE \033[1;30;40m")
					elif re.status_code == 403:
						print ("\033[1;34;40m"+str(i)+"\033[1;30;40m"+" == "+"\033[1;33;40m BLOCK \033[1;30;40m")
					elif re.status_code == 404:
						with open('die.txt','a') as die:
							die.write(str(i)+'\n')
						print ("\033[1;34;40m"+str(i)+"\033[1;30;40m"+" == "+"\033[1;31;40m DIE \033[1;30;40m")
				except Exception:
					with open('die.txt','a') as die:
						die.write(str(i)+'\n')
					print("\033[1;34;40m"+str(i)+"\033[1;30;40m"+" == "+"\033[1;31;40m DIE \033[1;30;40m")
					pass
	else:
		print (" command unknown")
	print ("\033[1;32;40m thanks for using this tools :) \033[1;30;40m")

while True:
	banner()
	main()
