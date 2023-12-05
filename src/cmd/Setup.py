import os, shutil

def Install():
    build_output = open("Build_Output.json","r").read()
    input("All data is loaded! Press Enter to install. (3.8 mb)")
    
    paths = [ os.path.join("C:", "LegendEyeGameStudio"),
            os.path.join("C:/LegendEyeGameStudio", "VEye-Engine"),
            os.path.join("C:/LegendEyeGameStudio/VEye-Engine", "Project"),
            os.path.join("C:/LegendEyeGameStudio/VEye-Engine", "Application") ]
    for path in paths:
        print(path)
        try:
            os.mkdir(path)
        except FileExistsError:
            continue
    print("Writing ...")
    f_ = open("C:/LegendEyeGameStudio/VEye-Engine/Build_Output.json","w")
    f_.write(build_output)
    shutil.copyfile("VisionE.exe","C:/LegendEyeGameStudio/VEye-Engine/Application/VisionE.exe")
    
    input("""-------------------------All process is success!-------------------------
But you need add 'C:\LegendEyeGameStudio\VEye-Engine\Application' to path\n""")

Install()