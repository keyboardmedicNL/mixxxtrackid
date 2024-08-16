import pyautogui
import time

# variables
windows = pyautogui.getAllWindows()
txtFile = open("SongTitle.txt", "w")
title_array = []

print("Getsongtitle is running")

# clears SongTitle.txt on startup
with open("SongTitle.txt", "w") as txtfile:
    txtfile.write("")

# main loop
while 1:
    time.sleep(1)
    for window in windows:
        if "| Mixxx" in window.title: #Alternatively Mixxx, but | Mixxx avoids detecting other windows
            title = window.title
            title = title.removesuffix(" | Mixxx")
            title = title.removesuffix("Mixxx")
            title = title.removeprefix("MixxxSongTitle")
            if len(title_array) < 1:
                title_array.append(title)
                print(title_array)
                with open("SongTitle.txt", "w") as txtfile:
                        txtfile.write(title_array[0])
            elif len(title_array) == 1:
                if title_array[0] != title:
                    title_array.append(title)
                    print(title_array)
                    with open("SongTitle.txt", "w") as txtfile:
                        txtfile.write(title_array[1] + "\n")
                        txtfile.write("Mixed from: \n")
                        txtfile.write(title_array[0] + "\n")
            elif title != title_array[1] :
                title_array.append(title)
                del title_array[0]
                print(title_array)
                with open("SongTitle.txt", "w") as txtfile:
                        txtfile.write(title_array[1] + "\n")
                        txtfile.write("Mixed from: \n")
                        txtfile.write(title_array[0] + "\n")