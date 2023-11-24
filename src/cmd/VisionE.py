import os,json,sys



def create_project():
    project_name = sys.argv[2]
    path = os.path.join(".",project_name)
    try:
        os.mkdir(path)
    except:
        pass
    main_file = open(path+"/Main.py","w")
    main_file.write("# Import\nfrom Engine import *\n# Initial\ndisplay = Display(1000,600,DISPLAY_CAPTION)\n\n# Functional\n\n# Main\ndef f_MAIN():\n    while display.Enable:\n        display.Input()\n        display.Update()\n        # Code\n\n        display.Render()\nf_MAIN()")
    source_engine = open("C:/LegendEyeGameStudio/VEye-Engine/Build_Output.json","r").read()
    data = json.loads(source_engine)
    try:
        os.mkdir(path+"/Engine")
    except FileExistsError:
        pass
    for file in data:
        f_ = open(path+f"/Engine/{file['Name']}","w")
        f_.write(file["Content"])
    Run_file_src = '''import os\n\ndef Run():\n    while True:\n        input("Press 'Enter' to run.")\n        os.system("python Main.py")\nRun()'''
    run_file = open(path+"/Run.py","w")
    run_file.write(Run_file_src)
    print(f"Project '{project_name}' is created!")


def main():
    if sys.argv[1] == "init":
        create_project()
main()