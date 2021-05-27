# Slave Device


from machine import Pin, I2C
import time

pin = Pin(25, Pin.OUT)

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
i2c.init(I2C.SLAVE, addr=0x42)
data = bytearray(3)

# Signal start up
for x in range(10):
	pin.toggle()
	time.sleep_ms(100)

# Start waiting for timing pulses
while True:
	pin.toggle()
	i2c.recv(data)
	time.sleep_ms(100)