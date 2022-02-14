import json
import os
from turtle import title
from xmlrpc.client import boolean
import sys
import tkinter as tk
from tkinter import filedialog

class style:
    style.DEF = '--  '
    style.WARN = '??  '
    style.OK = '))  '
    style.FAIL = '!!  '
    style.FAINT = "  "
    style.BOLD = ""
    style.ENDC = ''

if os.name == "Darwin":
    style.DEF = '\033[36m'
    style.WARN = '\033[33m'
    style.OK = '\033[0;32m'
    style.FAIL = '\033[31m'
    style.FAINT = "\033[2m"
    style.BOLD = "\033[1m"
    style.ENDC = '\033[0m'

# Choosing File
root = tk.Tk()
root.withdraw()
print(f"{style.CYAN}{style.BOLD}Please choose a file to convert: {style.ENDC}")
print(f"{style.CYAN}{style.FAINT}(file explorer opening...){style.ENDC}")
chosen = filedialog.askopenfilenames(title='select', filetypes=[("JSON", ".json")])
print(f"{style.CYAN}{style.FAINT}Chosen file:  {chosen}{style.ENDC}")

# Recieve lang code & Setting file name
langCode = input(f"{style.CYAN}Enter language code: {style.ENDC}")
originPath = "./exports"
fileNamePrefix = "TheLanguage"
fileName = f"{fileNamePrefix}.{langCode}.resx"
overwrite = False
openFlag = ""

# Check if file already exist and deal w consquences
if os.path.exists(f"{originPath}/{fileName}"):
    permission = input(f"{style.WARN}{style.BOLD}The file  {fileName}  already exists. Would you like it to be overwritten? (Y/n): {style.ENDC}")
    if permission == "Y" or permission == "y":
        print(f"{style.CYAN}Awesome! Converting and overwriting now...{style.ENDC}")
        openFlag = "w"
    else:
        sys.exit(f"{style.FAIL}{style.BOLD}Conversion cancelled. Please try again with a different language code.{style.ENDC}")
else:
    print(f"{style.CYAN}Beginning conversion...{style.ENDC}")
    print(f"{style.CYAN}...{style.ENDC}")
    openFlag = "x"

# Create or open file
open(f"{originPath}/{fileName}", openFlag, encoding="utf8")
edit = open(f"{originPath}/{fileName}", "a", encoding="utf8")
print(f"{style.CYAN}...{style.ENDC}")

# Execute conversion
with open(chosen[0], "r", encoding="utf8") as og:
    ogDict = json.load(og)
for attribute, value in ogDict.items():
    edit.write(f'<data name="{attribute}" xml:space="perserve">\n      <value>{value}</value>\n  </data>\n')
print(f"{style.CYAN}...{style.ENDC}")

#Success message
print(f"{style.OK}{style.BOLD}SUCCESS! You will find your RESX file in the {originPath} folder (or your custom path).{style.ENDC}")
