from smbus2 import SMBus
from bme280 import BME280
import cv2 as cv
import sys
import math
from ltr559 import LTR559
import time
import os

bus = SMBus(1)
ltr559 = LTR559()
bme280 = BME280(i2c_dev=bus)
min_temp = 0
max_temp = 0
min_lux = 0
max_lux = 0
height = 480
width = 480
valid_options = ["aloe", "lemon", "pepper", "tomato"]
plant = None
while plant == None:
    print("\nPlease choose a plant from the list:")
    for i, option in enumerate(valid_options):
        print(f"{i+1}. {option}")
    user_input = input("Enter your choice as a number or name: ").lower()

    if user_input in valid_options:
        plant = user_input
    elif user_input.isdigit and 1 <= int(user_input) <= len(valid_options):
        plant = valid_options[int(user_input) - 1]
    else:
        print(f"Invalid choice, try again.")

print(f"you chose {plant}!")

if plant == "aloe": # Setting the parameters based on the chosen plant, need to do more research and testing before setting these.
    min_lux = 1000
    min_temp = 50
    max_lux = 5000
    max_temp = 86
elif plant == "lemon":
    min_lux = 7500
    min_temp = 60
    max_lux = 15000
    max_temp = 95
elif plant == "pepper":
    min_lux = 1200
    min_temp = 59
    max_lux = 4000
    max_temp = 85
elif plant == "tomato":
    min_lux = 5000
    min_temp = 59
    max_lux = 10000
    max_temp = 85

temperature = (bme280.get_temperature() * 1.8) + 21 #Formula to change temp to F. Will put this in a loop eventually.
lux = (ltr559.get_lux() * 4) #Should be CLOSE to the true lux on the sensor.
key = None
img = cv.imread("images/blank.png")
cv.imshow("Plant Mood", img)
key = cv.waitKey(2)

if plant == "aloe":
    while key != ord("e"):
        key = cv.waitKey(2)
        temperature = (bme280.get_temperature() * 1.8) + 21 
        lux = (ltr559.get_lux() * 4)
        if min_temp <= temperature <= max_temp and min_lux <= lux <= max_lux:
            img = cv.imread("images/happy_aloe.png")
            cv.imshow("Plant Mood", img)
            time.sleep(1.0)
            print(f"Light = {lux} and temperature = {temperature}")
        else:
            img = cv.imread("images/sad_aloe.png")
            cv.imshow("Plant Mood", img)
            time.sleep(1.0)
            print(f"Light = {lux} and temperature = {temperature}")
if plant == "lemon":
    while key != ord("e"):
        key = cv.waitKey(2)
        temperature = (bme280.get_temperature() * 1.8) + 21
        lux = (ltr559.get_lux() * 4)
        if min_temp <= temperature <= max_temp and min_lux <= lux <= max_lux:
            img = cv.imread("images/happy_lemon.png")
            resized = cv.resize(img, (width, height))
            cv.imshow("Plant Mood", resized)
            time.sleep(1.0)
            print(f"Light = {lux} and temperature = {temperature}")
        else:
            img = cv.imread("images/sad_lemon.png")
            resized = cv.resize(img, (width, height))
            cv.imshow("Plant Mood", resized)
            time.sleep(1.0)
            print(f"Light = {lux} and temperature = {temperature}")
if plant == "pepper":
    while key != ord("e"):
        key = cv.waitKey(2)
        temperature = (bme280.get_temperature() * 1.8) + 21
        lux = (ltr559.get_lux() * 4)
        if min_temp <= temperature <= max_temp and min_lux <= lux <= max_lux:
            img = cv.imread("images/happy_pepper.png")
            cv.imshow("Plant Mood", img)
            time.sleep(1.0)
            print(f"Light = {lux} and temperature = {temperature}")
        else:
            img = cv.imread("images/sad_pepper.png")
            cv.imshow("Plant Mood", img)
            time.sleep(1.0)
            print(f"Light = {lux} and temperature = {temperature}")
if plant == "tomato":
    while key != ord("e"):
        key = cv.waitKey(2)
        temperature = (bme280.get_temperature() * 1.8) + 21
        lux = (ltr559.get_lux() * 4)
        if min_temp <= temperature <= max_temp and min_lux <= lux <= max_lux:
            img = cv.imread("images/happy_tomato.png")
            resized = cv.resize(img, (width, height))
            cv.imshow("Plant Mood", resized)
            time.sleep(1.0)
            print(f"Light = {lux} and temperature = {temperature}")
        else:
            img = cv.imread("images/sad_tomato.png")
            resized = cv.resize(img, (width, height))
            cv.imshow("Plant Mood", resized)
            time.sleep(1.0)
            print(f"Light = {lux} and temperature = {temperature}")
cv.destroyAllWindows()
restart = input("Type R for restart or E to exit" + "\nInput: ").lower()	
if restart == "r":
	os.execv(sys.executable, ['python'] + sys.argv)
else:
	exit()
