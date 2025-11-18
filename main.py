from smbus2 import SMBus
from bme280 import BME280
import cv2

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)
min_temp = 0
max_temp = 0
min_lux = 0
max_lux = 0
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
    min_lux = 1
    min_temp = 1
    max_lux = 1
    max_temp = 1
elif plant == "lemon":
    min_lux = 1
    min_temp = 1
    max_lux = 1
    max_temp = 1
elif plant == "pepper":
    min_lux = 1
    min_temp = 1
    max_lux = 1
    max_temp = 1
elif plant == "tomato":
    min_lux = 1
    min_temp = 1
    max_lux = 1
    max_temp = 1

temperature = (bme280.get_temperature() * 1.8) + 32 #Formula to change temp to F. Will put this in a loop eventually.
    