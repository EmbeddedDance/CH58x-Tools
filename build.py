import os


project_path = os.getcwd()
if os.path.basename(project_path) == "tools":
    project_path = os.path.dirname(project_path)

os.chdir(project_path)

if not os.path.exists("build"):
    print("Not Found build folder, creating...")
    os.mkdir("build")
else:
    print("Found build folder")

os.chdir("build")

build_cmd = "cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 -GNinja .. && ninja"
os.system(build_cmd)
