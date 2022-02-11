# JSON -> RESX CONVERTER
For the best reading experience right click this README.md file in the file navigator and select `Open Preview`.

<br >

### ( ! ) PREREQUISITES:
- Python 3+ must be installed on your machine.

<br >

## HOW TO USE

1.  Within the terminal or command prompt, navigate into the JSON-RSEX-CONVERTER folder. 
    Once inside, run the python command followed by the converter file name.
    #### MAC OS:
    `python3 converter.py`

    #### WINDOWS OS:
    `python converter.py`

2. After running the above command, the app should walk you through all the steps. 
If you wish to change the path of export, see the instructions below.



<br >
<br >

## CHANGING EXPORT PATH / LOCATION
Currently the export target path is set to the export folder that is within the `JSON-RESX-CONVERTER` folder.
This can be changed by adjusting the `originPath` variable.
<br >
( ! ) NOTE: The path starts from its current position. See below:
```
originPath = "./exports"
Adjust this---|________|

Example:
orginPath = "../resources/resx-files"
```