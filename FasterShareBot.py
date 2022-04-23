import ssl, os, requests, time
from threading import active_count, Thread
from pystyle import Colorate, Colors, Write
from random import randint, choice
from urllib3.exceptions import InsecureRequestWarning
from http import cookiejar
from Data.UserAgent import UserAgent
from Data.Lists import DeviceTypes, Platforms, Channel, ApiDomain


class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r = requests.Session()
SentTotalSentShares = 0
TotalFailedReq = 0

r.cookies.set_policy(BlockCookies())


def Clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    else:
        pass

def ReadFile(filename, method):
    with open(filename, method, encoding='utf8') as f:
        content = [line.strip('\n') for line in f]
        return content


def SendView(item_id):
    global SentTotalSentShares, TotalFailedReq, DebugMode
    platform = choice(Platforms)
    osVersion = randint(1, 12)
    DeviceType = choice(DeviceTypes)
    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": choice(UserAgent)
    }
    appName = choice(["tiktok_web", "musically_go"])
    Device_ID = randint(1000000000000000000, 9999999999999999999)
    apiDomain = choice(ApiDomain)
    channelLol = choice(Channel)
    URI = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
    Data = f"item_id={item_id}&share_delta=1"
    try:
        req = r.post(URI, headers=headers, data=Data, stream=True, verify=False)
    except:
        pass


def ClearURI(link):
    if "vm.tiktok.com" in itemID or "vt.tiktok.com" in itemID:
        return \
        r.head(itemID, stream=True, verify=False, allow_redirects=True, timeout=5).url.split("/")[5].split("?", 1)[0]
    else:
        return itemID.split("/")[5].split("?", 1)[0]


if __name__ == "__main__":
    Clear()
    itemID = Write.Input("Video Link > ", Colors.red_to_purple, interval=0.0001)
    amount = Write.Input("Amount (0=inf) > ", Colors.red_to_purple, interval=0.0001)
    NThread = Write.Input("Thread Amount > ", Colors.red_to_purple, interval=0.0001)

    itemID = ClearURI(itemID)

    if int(amount) == 0:
        for i in range(1, int(NThread)):
            Thread(target=(lambda itemID: [SendView(itemID) for i in iter(bool, True)]), args=(itemID,)).start()
    else:
        while SentTotalSentShares < int(amount):
            if active_count() <= int(NThread):
                try:
                    Thread(target=SendView, args=(itemID,)).start()
                except:
                    pass
