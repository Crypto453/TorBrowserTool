import os 
import colorama
from colorama import Fore
import random
import time
from time import sleep

def full_funtion():
	os.system("clear")
	os.system("python3 banner")
def list():
	list_a = ["\n[1] Download for Windows", "[2] Download for macOS", "[3] Download for Linux", "[4] Download for android", "[5] EXIT"]
	for list_x in list_a:
		print(Fore.MAGENTA + list_x)
		sleep(0.3)
def url():
	print(Fore.GREEN + ">>> " + Fore.MAGENTA + "https://www.torproject.org/ \n https://donate.torproject.org/" + Fore.GREEN + " <<< ")
full_funtion()
url()
list()
tor_tor = int(input(Fore.MAGENTA + "===> "))
if tor_tor == 1:
	print("Descargando archivo......")
	os.system("wget -i https://www.torproject.org/dist/torbrowser/10.5.10/torbrowser-install-win64-10.5.10_en-US.exe")
elif tor_tor == 2:
	print("Descargando archivo")
	os.system("wget -i https://www.torproject.org/dist/torbrowser/10.5.10/TorBrowser-10.5.10-osx64_en-US.dmg")
elif tor_tor == 3:
	print("Descargando archivo")
	os.system("wwget -i https://www.torproject.org/dist/torbrowser/10.5.10/tor-browser-linux64-10.5.10_en-US.tar.xz")
elif tor_tor == 4:
	print("Descargando archivo")
	os.system("wget -i https://www.torproject.org/download/#android")
else:
	print(Fore.RED + "Orden no encontrada, Intentelo denuevo")

