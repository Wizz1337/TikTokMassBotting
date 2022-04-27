import os, sys

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    else:
        pass

def set_console_title(Content):
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

def read_file(filename,method):
    with open(filename,method,encoding='utf8') as f:
        content = [line.strip('\n') for line in f]
        return content

def read_proxies_file():
    restartTry = True
    path = os.path.join("Data", "Proxies.txt")
    while restartTry:
        try:
            proxies = read_file(path, 'r')
            restartTry = False
            return proxies
        except:
            print("Failed to open Proxies.txt")
            restartTry = True