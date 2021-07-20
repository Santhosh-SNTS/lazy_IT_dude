import pyautogui
import time


pyautogui.FAILSAFE = False
print("\n██╗      █████╗ ███████╗██╗   ██╗    ██╗████████╗    ██████╗ ██╗   ██╗██████╗ ███████╗\n"
"██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝    ██║╚══██╔══╝    ██╔══██╗██║   ██║██╔══██╗██╔════╝\n"
"██║     ███████║  ███╔╝  ╚████╔╝     ██║   ██║       ██║  ██║██║   ██║██║  ██║█████╗\n"  
"██║     ██╔══██║ ███╔╝    ╚██╔╝      ██║   ██║       ██║  ██║██║   ██║██║  ██║██╔══╝\n"  
"███████╗██║  ██║███████╗   ██║       ██║   ██║       ██████╔╝╚██████╔╝██████╔╝███████╗\n"
"╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═╝   ╚═╝       ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝\n")

print("This program was developed by SANTHOSH-SNTS\n\n")

print("[+] This is the life saving hack for (Work From Home) employee, this program will keep your screen alive...\n ")
print("\t[+] LAZY IT DUDE is turned ON \n\t[+] Mouse will be moved that won't let your computer screen down \n\t[+] To quit this program press ctrl+c ")
print("\n(NOTE : Your mouse is in the left top corner of your screen)\n  \t60 sec  = 1 minute\n  \t300 sec = 5 minutes ")

try:
    counts = input("\n[+] Please enter the number of seconds (eg: 15) : ")
    print("\n[+] Your mouse will be moved for every " + counts + " second\n")
except KeyboardInterrupt:
    print("\n\n[+] Detected ctrl + c.............................. Quitting lazy IT dude Developed by SANTHOSH")


def mouse(counts):
    time.sleep(counts)
    # pyautogui.moveRel(0, 50, duration=5)
    # pyautogui.moveRel(0, -50, duration=5)
    for i in range(0, 50):
        pyautogui.moveTo(0, i * 5)
    for i in range(0, 3):
        pyautogui.press('shift')


try:
    times_count = 0
    while True:

        mouse(int(counts))
        times_count = times_count + 1

        print("\r        [+] Mouse moved count : " + str(times_count), end="")

except KeyboardInterrupt:
        print("\n\n[+] Detected ctrl + c.............................. Quitting lazy IT dude Developed by SANTHOSH")
