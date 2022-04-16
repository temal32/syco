import sys
import requests
import psutil
import platform
import subprocess


class value:
    global first, second, third
    first = False
    second = False
    third = False

length = len(sys.argv)

client_version = "1.1 BETA VERSION"
uname = platform.uname()

if len(sys.argv) < 1:
    print("Error: 0 arguemnts given")
elif len(sys.argv) == 1:
    print("No arguments given, type syco help for help.")
    exit()
else:
    try:
        if sys.argv[1]:
            first = True
            value_first = str(sys.argv[1])
        else:
            pass
    except:
        pass
    try:
        if sys.argv[2]:
            second = True
            value_second = str(sys.argv[2])
        else:
            pass
    except:
        pass
    try:
        if sys.argv[3]:
            third = True
            value_third = str(sys.argv[3])
        else:
            pass
    except:
        pass

class functions:
    def download(self):
        print("Starting...")
        try:
            url = value_second
            try:
                r = requests.get(url)
            except:
                print("Error: Invalid URL")
            print(f"Stats:")
            print(r.status_code)
            filepath = value_third
            try:
                with open(filepath, 'wb') as f:
                    f.write(r.content)
                    print("Done!")
            except:
                print("Error: Invalid path and/or filename!")
            # print(r.headers['content-type'])
        except:
            print("Could not download!")

if first == True:
    if value_first == "download":
        if second == True:
            if third == True:
                functions.download(self=True)
            else:
                print("Error: No download path set")
        else:
            print("Error: Nothing given to download")
            print("Error: No download path set")
    elif value_first == "help":
        print("Available commands:")
        print("1. help, shows help and commands for this program")
        print("2. info, shows information about the current installed program")
        print("3. download, downloads a file (download, filelink, filepath)")
        print("4. rev, reveals content of (cpu, gpu, ram, sys, desk, mach)")
    elif value_first == "info":
        print("Temal.cf SystemControlling (Sy-Co)")
        print(f"Version: {client_version}")
        print(f"Rep: github.com/temal32/syco")
    elif value_first == "rev":
        if second == True:
            target = value_second
            if target == "gpu":
                output = subprocess.check_output("wmic path win32_VideoController get name", shell=True)
                output = output.decode("utf-8")
                print(output)
            elif target == "cpu":
                import cpuinfo
                print(cpuinfo.get_cpu_info()['brand_raw'])
                print(f"Physical cores: {psutil.cpu_count(logical=False)}")
                print(f"Logical cores: {psutil.cpu_count(logical=True)}")
            elif target == "sys":
                print(f"Operating system: {uname.system}")
                print(f"Release: {uname.release}")
                print(f"Version: {uname.version}")
            elif target == "desk":
                print(uname.node)
            elif target == "mach":
                print(uname.machine)
            elif target == "ram":
                output = subprocess.check_output("wmic memorychip get devicelocator", shell=True)
                output = output.decode("utf-8")
                print(output)
                print("\033[A                             \033[A")
                print(f"Total: {round(psutil.virtual_memory().total / 1000000000, 2)} GB")
                print(f"Available: {round(psutil.virtual_memory().available / 1000000000, 2)} GB")
                print(f"Used: {round(psutil.virtual_memory().used / 1000000000, 2)} GB")
                print(f"Usage: {psutil.virtual_memory().percent}%")
            else:
                print("Cannot get details about this device!")
        else:
            print("Nothing given to reveal.")
    else:
        print("Error: unknown command")