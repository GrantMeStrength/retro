# Testing


from machine import Pin, I2C
import time

pin = Pin(25, Pin.OUT)

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
devices = i2c.scan()
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

# Signal start up
for x in range(10):
	pin.toggle()
	time.sleep_ms(100)

# Start sending timing pulses
while True:
	pin.toggle()
	i2c.writeto(76, b'123')
	time.sleep_ms(1000)
