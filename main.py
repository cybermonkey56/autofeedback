import pyautogui
import pandas as pd
flag = 1
df = pd.read_csv('data.csv')
print(df)
while flag == 1:
    pyautogui.PAUSE = 0.001
    pyautogui.press('tab')
    pyautogui.press('5')
#