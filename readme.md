# what is it:
a very simple script that reads the titlebar of Mixxx and saves the current trackid from it to a file. when the tracks change it will append the new track to the file and show the old track it was mixed out of, it will continue doing this everytime you change tracks not showing more then 2 tracks at a time.

Example:
```
Sandstorm - Darude
Mixed from:
TNT - ACDC
```

this text file can be loaded into obs to show current track id's for dj streams.

# how to use:
- install python (https://www.python.org/) on your system and make sure to select "add to path" when installing
- needs the pip modules ```pyautogui``` and ```time```, if you dont have these installed you can install them with pip (https://pypi.org/project/pip/)
- run the script either trough a terminal window or trough the included batch file for windows users

Aditional notes   
* make sure you launch the script after you launch Mixxx
* the file gets cleared on every restart of the script
* should work on linux also, currently only tested on windows 10