import os
import sys
import subprocess
from pyfuf import binary_path
import time

binary_name = "fuff.exe" if sys.platform == "win32" else "fuff"

def check_fuff_installed():
    return os.path.exists(binary_path)

def get_binary_path():
    return binary_path

def install_fuff():
    print("Installing fuff...")
    if sys.platform == "win32":
        subprocess.run(["powershell", "Invoke-WebRequest", "-Uri", "https://github.com/0xleft/pypifuf/raw/master/bin/windows_fuff.exe", "-OutFile", binary_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.run(["wget", "https://github.com/0xleft/pypifuf/raw/master/bin/linux_ffuf", "-O", binary_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.chmod(binary_path, 0o755)
    print(f"fuff installed. Path: {binary_path}")
    time.sleep(2)