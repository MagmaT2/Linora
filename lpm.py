import os
import sys

def install_package(package_name):
    os.system(f"pip install {package_name}")

def uninstall_package(package_name):
    os.system(f"pip uninstall {package_name}")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        command = sys.argv[1]
        package = sys.argv[2]
        if command == "install":
            install_package(package)
        elif command == "uninstall":
            uninstall_package(package)
        else:
            print("Error: Unknown command.")
    else:
        print("Usage: lpm <install|uninstall> <package>")