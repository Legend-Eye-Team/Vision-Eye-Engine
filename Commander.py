# a = [
#     {"Name":"a.py","Content":"print(123)" }
# ]

import os,json

exited = False

def BMVer():
    Name = "Build_Output.json"
    data = []
    for filename in os.listdir(os.getcwd() + "\\src"):
        try:
            with open(os.path.join(os.getcwd()+"\\src", filename), 'r') as f: # open in readonly mode
                data.append({"Name":filename,"Content":f.read()})
        except:
            continue
    new_version_build = open(Name,"w")
    new_version_build.write(json.dumps(data,indent=4))

def OpenPVer(folder,custom=""):
    f = open(custom+"Build_Output.json","r").read()
    data = json.loads(f)
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass
    for file in data:
        f_ = open(f"{folder}/{file['Name']}","w")
        f_.write(file["Content"])

def CreateProject():
    OpenPVer()
    name = input("Name?>")
    main = open(name,"w")

def AutoBuild():
    global exited
    while True:
        c = input("Input 'e' to exit>")
        if c.lower() == "e": 
            exited = True
            break

        BMVer()
        OpenPVer("Engine")
        os.system("python Main.py")

def DeveloperMenu():
    global exited
    
    while not exited:
        print("""+--------------------------+
|      DEVELOPER MENU      |
+--------------------------+
| (BNV,1) : Build New Ver  |  
| (IED,2) : Init Env Dev   | 
| (OPV,3) : Open Prev Ver  |
| (AUTO,4): Auto Build     |  
| (EXIT,0): EXIT           |  
| Please Press Number Or   |
| Command                  |
+--------------------------+""")
        option = input("DEV?>")
        option = option.upper()
        if option == "1" or option == "BNV":
            BMVer()
        elif option == "2" or option == "IED":
            # LPVer()
            print("unknown")
        elif option == "3" or option == "OPV":
            OpenPVer("Src/Engine")
        elif option == "4":
            AutoBuild()
        elif option == "0" or option == "EXIT":
            exited = True

def ProjectMenu():
    global exited
    
    while not exited:
        print("""+--------------------------+
|       PROJECT MENU       |
+--------------------------+
| (CRN,1) : Create New     |  
| (OP,2)  : Open Project   | 
| (EXIT,0): EXIT           |  
| Please Press Number Or   |
| Command                  |
+--------------------------+""")
        option = input("DEV?>")
        option = option.upper()
        if option == "1" or option == "CRN":
            OpenPVer("Engine","C:\LegendEyeGameStudio\VEye-Engine\\")
            main_file = open("Game.py","w")
            f = "# Import\nfrom Engine import *\n# Initial\ndisplay = Display(1000,600,DISPLAY_CAPTION)\n\n# Functional\n\n# Main\ndef f_MAIN():\n    while display.Enable:\n        display.Input()\n        display.Update()\n        # Code\n\n        display.Render()\nf_MAIN()"
            main_file.write(f)
            print(f)
            print("finally")
        elif option == "2" or option == "OP":
            # LPVer()
            print("unknown")
        elif option == "0" or option == "EXIT":
            exited = True


if __name__ == "__main__":
    while not exited:
        print("""+--------------------+
|        Menu        |
+--------------------+
| (1): Project       |
| (2): Dev Engine    |
| (0): Exit          |
+--------------------+""")
        change = input("MAIN?>")
        if change == "1":
            ProjectMenu()
        elif change == "2":
            DeveloperMenu() 
        elif change == "0":
            exited = True