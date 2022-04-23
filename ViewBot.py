import ssl, os, requests
from threading import active_count, Thread
from pystyle import Colorate, Colors, Write
from random import randint, choice
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
from http import cookiejar
from Data.UserAgent import UserAgent
from Data.Lists import DeviceTypes, Platforms, Channel, ApiDomain
import sys

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r                                 = requests.Session()
ThreadCount                       = 0
TotalSendedView                   = 0
TotalFailedReq                    = 0
ShareChoice                       = True
ViewChoice                        = True
DebugMode                         = False

r.cookies.set_policy(BlockCookies())

def Clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    else:
        pass

def Title(Content):
    global DebugMode
    if os.name == 'posix':
        sys.stdout.write(f"\33]0;{Content}\a")
        sys.stdout.flush()
        return False
    elif os.name == 'nt':
        os.system(f"title {Content}")
        return False
    else:
        pass

def ReadFile(filename,method):
    with open(filename,method,encoding='utf8') as f:
        content = [line.strip('\n') for line in f]
        return content

def ReadProxiesFile():
    restartTry = True
    Path = "./Data/Proxies.txt"
    while restartTry:
        try:
            proxies = ReadFile(Path, 'r')
            restartTry = False
            return proxies
        except:
            print(Colorate.Horizontal(Colors.red_to_white, f"Failed to open Proxies.txt"))
            Path = Write.Input("Proxies Path > ", Colors.red_to_purple, interval=0.0001)
            restartTry = True


def SendView(item_id, proxy, timeout, proxytype):
    global TotalSendedView, TotalFailedReq, DebugMode
    proxy         = {f'{proxytype}': f'{proxytype}://{proxy}'}
    platform      = choice(Platforms)
    osVersion     = randint(1, 12)
    DeviceType    = choice(DeviceTypes)
    headers       = {
                        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "user-agent": choice(UserAgent)
                    }
    appName       = choice(["tiktok_web", "musically_go"])
    Device_ID     = randint(1000000000000000000, 9999999999999999999)
    apiDomain     = choice(ApiDomain)
    channelLol    = choice(Channel)
    URI           = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
    Data          = f"item_id={item_id}&play_delta=1"

    try:
        req = r.post(URI, headers=headers, data=Data, proxies=proxy,timeout=timeout, stream=True, verify=False)
        try:
            if (req.json()["status_code"] == 0):
                TotalFailedReq += 1
                Title(f"Thread :{str(active_count()-1)} / Total Try :{TotalFailedReq}")
            else:
                pass
        except:
            TotalSendedView += 1
            print(Colorate.Horizontal(Colors.green_to_white, f"Sended View/Share: {TotalSendedView}"))
            Title(f"Thread :{str(active_count()-1)} / Total Try :{TotalFailedReq}")
    except:
        pass

def ClearURI(link):
    ParsedURL = urlparse(itemID)
    host = ParsedURL.hostname.lower()
    #print(itemID)
    if "vm.tiktok.com" == host or "vt.tiktok.com" == host:
        UrlParsed = urlparse(r.head(itemID, stream=True, verify=False, allow_redirects=True, timeout=5).url)
        return UrlParsed.path.split("/")[3]
    else:
        UrlParsed = urlparse(itemID)
        return UrlParsed.path.split("/")[3]

if (__name__ == "__main__"):
    Clear()
    print(Colorate.Horizontal(Colors.red_to_white, f"Working But Slow !"))
    itemID       = Write.Input("Video Link > ", Colors.red_to_purple, interval=0.0001)
    amount       = Write.Input("Amount (0=inf) > ", Colors.red_to_purple, interval=0.0001)
    ScrapProxie  = Write.Input("Scrap Proxies [y/n] > ", Colors.red_to_purple, interval=0.0001)
    Proxytype    = Write.Input("Proxy Type > ", Colors.red_to_purple, interval=0.0001)
    Timeout      = Write.Input("Proxy Timeout > ", Colors.red_to_purple, interval=0.0001)
    NThread      = Write.Input("Thread Amount > ", Colors.red_to_purple, interval=0.0001)
    
    if Title("Proy Scrapper X-Proxy by NightFallGT") == True:
        Debug = Write.Input("Debug Fails [y/n] ? > ", Colors.red_to_purple, interval=0.0001)
        if Debug.lower().startswith("y"):
            DebugMode = True
        else:
            DebugMode = False

    if ScrapProxie.lower().startswith("y"):
        from Data.ScrapProxie import Start; Start()

    itemID = ClearURI(itemID)

    ProxyChoose = True
    while ProxyChoose:
        if Proxytype.lower().startswith("h"):
            Proxytype = "http"
            ProxyChoose = False
        elif Proxytype.lower().endswith("4"):
            Proxytype = "socks4"
            ProxyChoose = False
        elif Proxytype.lower().endswith("5"):
            Proxytype = "socks5"
            ProxyChoose = False
        else:
            ProxyChoose = True
            print("Invalid Proxy Type | Choose : Http, Socks4, Socks5")
            Proxytype = Write.Input("Proxy Type > ", Colors.red_to_purple, interval=0.0001)

    proxy = ReadProxiesFile()
    
    print(Colorate.Horizontal(Colors.red_to_white, f"Hit are not counted"))
    print(Colorate.Horizontal(Colors.red_to_white, f"Bot Started check your video view in 5 minute !"))

    if int(amount) == 0:
        while True:
            Run = True
            while Run:
                if active_count() <= int(NThread):
                    try:
                        Thread(target=(SendView), args=(itemID,choice(proxy),int(Timeout),Proxytype,)).start()
                    except:
                        pass
    else:
       while TotalSendedView < int(amount):
            if active_count() <= int(NThread):
                try:
                    Thread(target=(SendView), args=(itemID,choice(proxy),Timeout,Proxytype,)).start()
                except:
                    pass
