# import keyboard
import pyautogui
# import pytesseract
# from PIL import Image

# my_Screenshot = pyautogui.screenshot(region=(0, 100, 300, 400))
# my_Screenshot.save(r'test.png')


# Creating image object
# image = Image.open('test.png')

# Pass image into pytesseract module
# choose language for pytesseract
# image_to_text = pytesseract.image_to_string(image, lang="eng")

# print text from screenshot
# print(image_to_text)

# size of screen
# print(pyautogui.size())

# mouse position
# print(pyautogui.position())
try:
    while True:

        pyautogui.moveTo(900, 900, duration=0.5)
        pyautogui.moveTo(600, 200, duration=0.5)
        pyautogui.moveTo(50, 700, duration=0.5)

except KeyboardInterrupt:
    pass
