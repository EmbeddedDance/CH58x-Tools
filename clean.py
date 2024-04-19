import os
import shutil


project_path = os.getcwd()
if os.path.basename(project_path) == "tools":
    project_path = os.path.dirname(project_path)

os.chdir(project_path)

if not os.path.exists("build"):
    print("Not Found build folder, not need to clean")
else:
    print("Found build folder, cleaning...")
    try:
        os.rmdir("build")
    except Exception as e:
        try:
            shutil.rmtree("build")
        except Exception as e:
            print(e)
            print("Clean failed")
            exit(1)

    print("Cleaned build folder")
