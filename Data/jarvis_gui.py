import subprocess
import ctypes
import pyautogui

def open_chrome():
    # Launch Chrome
    subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", "--app=https://joykuttan.github.io/jarvis_ui.github.io/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for Chrome to open
    pyautogui.sleep(2)

    # Maximize Chrome window
    width, height = pyautogui.size()
    pyautogui.keyDown('win')
    pyautogui.press('up')
    pyautogui.keyUp('win')
    pyautogui.sleep(1)
    pyautogui.moveTo(0, 0)
    pyautogui.moveTo(width // 2, height // 2)

if __name__ == "__main__":
    open_chrome()

