#Publishing code with his copyright is skidding
#Reading code is not skidding.
#This is not my code im only publishing a leak

import requests, ssl
from threading import active_count, Thread
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
from random import randint


class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

r = requests.Session()
r.cookies.set_policy(BlockCookies())

def SendViews(id):
    try:
        r.post(f"https://api.toutiao50.com/aweme/v1/aweme/stats/?channel=googleplay&device_type=SM-G780G&device_id={randint(1000000000000000000, 9999999999999999999)}&os_version=10&version_code=220400&app_name=musically_go&device_platform=android&aid=1340", headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "user-agent": "com.zhiliaoapp.musically.go/220400 (Linux; U; Android 10; en_US; SM-G780G; Build/MMB25K.G9250ZTU5DPC5; Cronet/TTNetVersion:5f9540e5 2021-05-20 QuicVersion:47555d5a 2020-10-15)"}, data=f"item_id={item_id}&play_delta=1", stream=True, verify=False)
    except:
        pass
    
def Start():
    id = str(input("Video Link : "))

    if ("vm.tiktok.com" in id or "vt.tiktok.com" in id):
        id = r.head(id, stream=True, verify=False, allow_redirects=True).url.split("/")[5].split("?", 1)[0]
    else:
        id = id.split("/")[5].split("?", 1)[0]

    print("Started")

    while True:
        if (active_count() <= 1000):
            Thread(target=(SendViews), args=(id,)).start()

Start()
