from time import sleep

import pigpio


class LED:
    def __init__(self, gpio=None) -> None:
        if isinstance(gpio, type(None)):
            self.gpio_led = 21
            print(f"Connect to GPIO#{self.gpio_led}.")
        else:
            self.gpio_led = gpio
        self.pig = pigpio.pi()
        self.pig.set_mode(self.gpio_led, pigpio.OUTPUT)
    
    def on(self) -> None:
        self.pig.write(self.gpio_led, 1)
    
    def off(self) -> None:
        self.pig.write(self.gpio_led, 0)

    def status(self) -> int:
        return self.pig.read(self.gpio_led)
    
    def blink(self, interval=1.0) -> None:
        self.on()
        sleep(interval)
        self.off()
        sleep(interval)


if __name__ == "__main__":
    try:
        led = LED()
        led.on()
        print(f"LED Status: {led.status()}")
        sleep(1)
        led.off()
        print(f"LED Status: {led.status()}")
        sleep(1)
        while True:
            led.blink()
            led.blink(2.5)
    except KeyboardInterrupt:
        led.off()
