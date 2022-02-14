# JSON -> RESX CONVERTER
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
If you wish to change the path of export, or the file name prefix, see the instructions below.



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

<br >
<br >

## CHANGING FILE NAME PREFIX
The defaault file name prefix is `TheLanguage` followed by user inputted language code.
This can be changed by adjusting the `fileNamePrefix` variable.
<br >

```
fileNamePrefix = "TheLanguage"
Adjust this------|___________|

Example:
fileNamePrefix = "LanguageResource"
```
