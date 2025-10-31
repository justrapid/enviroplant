from smbus2 import SMBus
from bme280 import BME280

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)
temperature =  (bme280.get_temperature() * 1.8) + 32
print(temperature)