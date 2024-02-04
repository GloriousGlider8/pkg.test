# This script will be installed as the cmdname property of your data.py file
import json
import colorama as c
argsTxt = open("data\\args.json", "r")
args = json.load(argsTxt)
argsTxt.close()
argsTxt = None

print("PKG works!")

temp = """argsTxt = open(\"data\\\\args.json\", \"r\")
args = json.load(argsTxt)
argsTxt.close()
argsTxt = None"""

print(c.Fore.GREEN + "Terminal + addons are working." + c.Style.RESET_ALL + "\nArgument Format:")
for i in range(len(args)):
    print("[" + str(i) + "]: " + args[i])
print(c.Fore.BLUE + "\nGet argument list with:\n" + c.Fore.LIGHTCYAN_EX + temp)
print(c.Fore.BLUE + "in your addon script." + c.Style.RESET_ALL)
