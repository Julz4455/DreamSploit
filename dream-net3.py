import os, sys, json, random
from termcolor import colored

if os.getuid() != 0:
    print("Must run as root")
    sys.exit(1)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
logo_p1 = """
     _______
    //    ) )
   //    / /  __      ___      ___      _   __
  //    / / //  ) ) //___) ) //   ) ) // ) )  ) )
 //    / / //      //       //   / / // / /  / /
//____/ / //      ((____   ((___( ( // / /  / /
"""

logo_p2 = """
.d8888. d8888b. db       .d88b.  d888888b d888888b
88'  YP 88  `8D 88      .8P  Y8.   `88'   `~~88~~'
`8bo.   88oodD' 88      88    88    88       88
  `Y8b. 88~~~   88      88    88    88       88
db   8D 88      88booo. `8b  d8'   .88.      88
`8888Y' 88      Y88888P  `Y88P'  Y888888P    YP
"""
randColor = random.choice(["grey", "red", "green", "yellow", "blue", "magenta", "cyan"])
randColor2 = random.choice(["grey", "red", "green", "yellow", "blue", "magenta", "cyan"])
print(colored(logo_p1, randColor)+colored(logo_p2, randColor2))
info = """
  \x1b[34mCodename\x1b[0m | \x1b[31mVersion\x1b[0m |       \x1b[32mGit Repo\x1b[0m
 ----------|---------|----------------------
  \x1b[32mPhoton\x1b[0m   | \x1b[34mv1.0.0\x1b[0m  | \x1b[31mJulz4455/DreamSploit\x1b[0m
"""
print(info)
didCommand = False
with open('modules3.json') as json_file:
    data = json.load(json_file)
    if 'modules' in data:
        modules = data['modules']
    else:
        print('Looks like your modules.json file is deformed. Fix it before using DreamSploit')
with open('allowed-linux.json') as json_file:
    data = json.load(json_file)
    if 'commands' in data:
        allowedLinuxCommands = data['commands']
    else:
        print('Looks like your allowed-linux.json file is deformed. Fix it before using DreamSploit')
while True:
    didCommand = False
    rawCommand = input('dream> ')
    dreamCommand = rawCommand.lower()
    commandList = open('modules.json')
    if dreamCommand == "help":
        print(colored("Command Help", "cyan"))
        print(colored("------------", "blue"))
        print(colored("""
        help         -- Show This Help Page
        show modules -- Show Modules
        module help  -- Show Module Install/Create Help
        """, "red"))
        didCommand = True
    elif dreamCommand == "exit":
        print("Exitting...")
        sys.exit()
    elif dreamCommand == "show modules":
        print(colored("Installed Modules", "cyan"))
        print(colored("-----------------", "blue"))
        for i in modules:
            print(i['name'])
            didCommand = True
    elif dreamCommand == "module help":
        print(colored("Installing/Creating Modules", "cyan"))
        print(colored("------------------", "blue"))
        print("1. For Creating: Create new module from template in the modules/ directory")
        print("2. Link the module in the modules.json file according to the template.json file")
        print("3. ")
        print("4. "+colored("Profit!", "green"))
        didCommand = True

    for i in modules:
        if dreamCommand == i['name']:
            exec(open(i['path']))
    for i in allowedLinuxCommands:
        if dreamCommand == i:
            print(os.popen(i).read())
            didCommand = True
    if didCommand == False:
        print("Command Not Found")
