from time import sleep
import pigpio

GPIO_SW = 27
GPIO_LED = 25

pig = pigpio.pi()
pig.set_mode(GPIO_LED, pigpio.OUTPUT)
pig.set_mode(GPIO_SW, pigpio.INPUT)
pig.set_pull_up_down(GPIO_SW, pigpio.PUD_DOWN)

def led(gpio):
    level = pig.read(gpio)
    pig.write(gpio, not level)

def sw(gpio, level, tick):
    led(GPIO_LED)

sw_button = pig.callback(GPIO_SW, pigpio.RISING_EDGE, sw)

try:
    while True:
        sleep(0.01)
except KeyboardInterrupt:
    pig.stop()
