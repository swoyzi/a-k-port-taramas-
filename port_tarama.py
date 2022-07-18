#!/usr/bin/env python

import os 

while True:

	print("""


____ _ _ _ ____ _   _ ___  _ 
[__  | | | |  |  \_/    /  | 
___] |_|_| |__|   |    /__ |

""")
	print("""
	gelişmiş tarama aracı

(1)Site hakkında genel bilgi 
(2)Hizli port taramasi
(3)Versiyon bilgisi
(4)SYN taraması
(5)TCP bağlantısı
(Q)exit 
""")

	islemno =  input("işlem numarasınıgir amk: ")
	if islemno=="1":
		hedefip= input ("Hedef siteyi gir mk: ")
		os.system("whois "+hedefip) 
	elif islemno=="2":
		hedefip= input ("Hedef siteyi gir mk: ")
		os.system("nmap "+hedefip)
	elif islemno=="3":
		hedefip= input ("Hedef siteyi gir mk: ")
		os.system("nmap -sV "+hedefip)
	elif islemno=="4":
		hedefip= input ("Hedef sitefyi gir mk: ")
		os.system("nmap  -sS "+hedefip)
	elif islemno=="5":
		hedefip= input ("Hedef siteyi gir mk: ")
		os.system("nmap -sT "+hedefip)
	elif islemno=="q" or islemno=="Q":
			quit()
	else:
		input("hatalı girdin orospu devam etmek  icin entere bas")
 