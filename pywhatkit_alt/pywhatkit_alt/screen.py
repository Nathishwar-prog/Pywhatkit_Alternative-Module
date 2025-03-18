import cv2
import numpy as np
import pyautogui

def record_screen(output="screen_record.mp4", duration=10, fps=20):
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output, fourcc, fps, screen_size)

    for _ in range(fps * duration):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

    out.release()


def take_screenshot(output="screenshot.png"):
    img = pyautogui.screenshot()
    img.save(output)
