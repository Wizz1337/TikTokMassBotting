import os, sys, time
import importlib.util

from utils import *

def packages_automation():
    
    names = ('pystyle', 'requests', 'threading', 'ssl', 'urllib3')

    for name in names:
        if name in sys.modules:
            print(f"{name!r} already in sys.modules")
        elif (spec := importlib.util.find_spec(name)) is not None:
            module = importlib.util.module_from_spec(spec)
            sys.modules[name] = module
            spec.loader.exec_module(module)
            print(f"{name!r} has been imported")
        else:
            print(f"can't find the {name!r} module")


if __name__ == '__main__':
    set_console_title("Launching Interface")
    clear_console()
    packages_automation()
    time.sleep(2)
    clear_console()
    os.execl(sys.executable, os.path.abspath('python "main.py"'), *sys.argv)
