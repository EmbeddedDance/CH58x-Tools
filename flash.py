import os
import subprocess
import re
import platform


project_path = os.getcwd()
if os.path.basename(project_path) == "tools":
    project_path = os.path.dirname(project_path)


project_name = os.path.basename(project_path)

device_location_id = ""
try:
    cmd = "ioreg -p IOUSB -l -w 0 | grep -B 5 -i '21984'"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, shell=True).stdout
    match = re.search(r"IOUSBHostDevice@(\w+)", result)
    if match:
        device_location_id = match.group(1)
except Exception as e:
    print("No device found")
    exit(1)

if device_location_id == "":
    print("No device found")
    exit(1)

hex_path = project_path + "/build/" + project_name + ".hex"
if os.path.exists(hex_path):
    try:
        if platform.system() == "Darwin":
            os.chdir(project_path + "/tools/macos")
            os.system(
                f"./WCHISPTool_CMD -p 0x{device_location_id} -c ch582_flash.config -o program -f {hex_path}"
            )
    except Exception as e:
        print(e)
        print("Flash failed")
        exit(1)
else:
    print("Hex file not found, please build project first")
    exit(1)
