from time import sleep
import pigpio

pig = pigpio.pi()
pig.set_mode(21, pigpio.OUTPUT)

try:
    while True:
        sleep(1)
        pig.write(21, 1)
        sleep(1)
        pig.write(21, 0)
except KeyboardInterrupt:
    pig.stop()
