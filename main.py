import cv2
import mediapipe as mp
import pyautogui 
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://chromedino.com/#google_vignette")

mp_solution = mp.solutions.hands
hand_detector = mp_solution.Hands(max_num_hands=1,)
drawing_utils = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

_,screenheight = pyautogui.size()

prev_y = None

while True:
    _,frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hands = hand_detector.process(rgb_frame)

    if hands.multi_hand_landmarks:
        for cordinates in hands.multi_hand_landmarks:
            drawing_utils.draw_landmarks(frame, cordinates, mp_solution.HAND_CONNECTIONS)

            index_finger = cordinates.landmark[8]
            y = index_finger.y * screenheight
            
            if prev_y is not None:
                if prev_y - y > 100:
                    pyautogui.press("space")
            
            prev_y = y


    cv2.imshow("Dino game main frame",frame)
    cv2.waitKey(1)