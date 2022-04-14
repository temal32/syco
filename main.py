import sys
import requests

class value:
    global first, second, third
    first = False
    second = False
    third = False

length = len(sys.argv)

client_version = "1.0 ALPHA VERSION"

if len(sys.argv) < 1:
    print("Error: 0 arguemnts given")
elif len(sys.argv) == 1:
    print("No arguments given, type temal help for help.")
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

#print(f"First Value is {first}, second value is {second}, third value is {third}")

if first == True:
    if value_first == "download":
        if second == True:
            if third == True:
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
                    #print(r.headers['content-type'])
                except:
                    print("Could not download!")
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
    elif value_first == "info":
        print("Temal.cf SystemControlling (Sy-Co)")
        print(f"Version: {client_version}")
        print(f"Rep: github.com/temal32/syco")
    else:
        print("Error: unknown command")