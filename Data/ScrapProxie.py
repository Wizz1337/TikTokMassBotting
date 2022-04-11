# All code from NightFallGT <3
# https://github.com/NightfallGT/X-Proxy
import threading, re, requests, os
from pystyle import Colorate, Colors
lock = threading.Lock()

def Title(Content):
    global DebugMode
    if os.name in ('posix', 'ce', 'dos'):
        print(Colorate.Horizontal(Colors.red_to_purple, f"{Content}"))
    elif os.name == 'nt':
        print(Colorate.Horizontal(Colors.red_to_purple, f"{Content}"))
        return False
    else:
        pass

class XProxy:
    proxy_w_regex = [
    ["http://spys.me/proxy.txt","%ip%:%port% "],
    ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"],
    ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","],
    ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
    ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'],
    ["https://www.us-proxy.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
    ["https://free-proxy-list.net/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
    ["https://www.sslproxies.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
    ['https://www.socks-proxy.net/', "%ip%:%port%"],
    ['https://free-proxy-list.net/uk-proxy.html', "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
    ['https://free-proxy-list.net/anonymous-proxy.html', "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
    ["https://www.proxy-list.download/api/v0/get?l=en&t=https", '"IP": "%ip%", "PORT": "%port%",'],
    ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all", "%ip%:%port%"],
    ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "%ip%:%port%"],
    ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
    ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt", "%ip%:%port%"],
    ["https://www.hide-my-ip.com/proxylist.shtml", '"i":"%ip%","p":"%port%",'],
    ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json", '"ip": "%ip%",\n.*?"port": "%port%",'],
    ['https://www.freeproxychecker.com/result/socks4_proxies.txt', "%ip%:%port%"],
    ['https://proxy50-50.blogspot.com/', '%ip%</a></td><td>%port%</td>'], 
    ['http://free-fresh-proxy-daily.blogspot.com/feeds/posts/default', "%ip%:%port%"],
    ['http://free-fresh-proxy-daily.blogspot.com/feeds/posts/default', "%ip%:%port%"],
    ['http://www.live-socks.net/feeds/posts/default', "%ip%:%port%"],
    ['http://www.socks24.org/feeds/posts/default', "%ip%:%port%"],
    ['http://www.proxyserverlist24.top/feeds/posts/default',"%ip%:%port%" ] ,
    ['http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http',"%ip%:%port%"],
    ['http://proxysearcher.sourceforge.net/Proxy%20List.php?type=socks', "%ip%:%port%"],
    ['http://proxysearcher.sourceforge.net/Proxy%20List.php?type=socks', "%ip%:%port%"], 
    ['https://www.my-proxy.com/free-anonymous-proxy.html', '%ip%:%port%'],
    ['https://www.my-proxy.com/free-transparent-proxy.html', '%ip%:%port%'],
    ['https://www.my-proxy.com/free-socks-4-proxy.html', '%ip%:%port%'],
    ['https://www.my-proxy.com/free-socks-5-proxy.html','%ip%:%port%'],
    ['https://www.my-proxy.com/free-proxy-list.html','%ip%:%port%'],
    ['https://www.my-proxy.com/free-proxy-list-2.html','%ip%:%port%'],
    ['https://www.my-proxy.com/free-proxy-list-3.html','%ip%:%port%'],
    ['https://www.my-proxy.com/free-proxy-list-4.html', '%ip%:%port%'],
    ['https://www.my-proxy.com/free-proxy-list-5.html','%ip%:%port%'],
    ['https://www.my-proxy.com/free-proxy-list-6.html','%ip%:%port%'],
    ['https://www.my-proxy.com/free-proxy-list-7.html','%ip%:%port%'],
    ['https://www.my-proxy.com/free-proxy-list-8.html','%ip%:%port%'],
    ['https://www.my-proxy.com/free-proxy-list-9.html','%ip%:%port%'],
    ['https://www.my-proxy.com/free-proxy-list-10.html','%ip%:%port%'],
    ]

    proxy_direct = [
        'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all',
        'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=5000&country=all&ssl=all&anonymity=all',
        'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=5000&country=all&ssl=all&anonymity=all',         
        'https://www.proxyscan.io/download?type=http',
        'https://www.proxyscan.io/download?type=https',
        'https://www.proxyscan.io/download?type=socks4',
        'https://www.proxyscan.io/download?type=socks5',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
        'https://github.com/TheSpeedX/PROXY-List/blob/master/socks4.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
        'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
        'https://multiproxy.org/txt_all/proxy.txt',
        'http://rootjazz.com/proxies/proxies.txt',
        'http://ab57.ru/downloads/proxyold.txt',
        'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
        'https://proxy-spider.com/api/proxies.example.txt',
        'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
        'https://www.proxy-list.download/api/v1/get?type=socks4'
        'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt'
        ]
                       

    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}

    def __init__(self):
        self.proxy_output = []
        self.scrape_counter = 0

    def file_read(self, name):
        with open(name, 'r', encoding='UTF-8') as f:
            text = [line.strip('\n') for line in f]
            return text

    def file_write(self, name, contents):
        with open(name, 'w', encoding='UTF-8' ) as f:
            for x in contents:
                f.write(x + '\n')

    def get_proxies(self):
        return self.proxy_output

class ProxyScrape(XProxy):
    def _scrape(self, url, custom_regex):
        try:
            proxylist = requests.get(url, timeout=5, headers=self.headers).text
            custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
            custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')

            for proxy in re.findall(re.compile(custom_regex), proxylist):
                self.proxy_output.append(proxy[0] + ":" + proxy[1])
                self.scrape_counter += 1
                
            Title(f"Scraped : {self.scrape_counter}")
        except:
            Title(f"Scraped : {self.scrape_counter}")

    def scrape_regex(self):
        for source in self.proxy_w_regex:
            self._scrape(source[0], source[1])

    def scrape_direct(self):
        for source in self.proxy_direct:
            try:
                page = requests.get(source, timeout=5, headers=self.headers).text
                for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), page):
                    self.proxy_output.append(proxy[0] + ':' + proxy[1])

            except:
                pass

def Start():
    p = ProxyScrape()
    print(Colorate.Horizontal(Colors.red_to_purple, f"Scraping Proxy"))
    p.scrape_regex()
    p.scrape_direct()
    output = p.get_proxies()
    clean_output = list(set(output))
    print(Colorate.Horizontal(Colors.red_to_purple, f"Length without duplicates : {len(clean_output)}"))

    print(Colorate.Horizontal(Colors.red_to_purple, f"Saved to Proxies.txt"))
    p.file_write('./Data/Proxies.txt', clean_output)
    
