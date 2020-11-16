import pyautogui
import time
msg = "bannez-moi"
count = 5
while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1
print("Fire in the hole!!!")
for i in range(0,int(20)):
    pyautogui.typewrite(msg + '\n')