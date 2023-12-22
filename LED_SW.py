from time import sleep

import pigpio

from LED import LED
from SW import SW


class LED_SW:
    def __init__(self, gpio_sw=None, gpio_led=None) -> None:
        self.pig = pigpio.pi()
        self.led = LED(gpio_led)
        self.sw = SW(gpio_sw)

    def attachment(self, gpio, level, tick):
        if not self.pig.read(self.led.gpio_led):
            self.led.on()
        else:
            self.led.off()

    def loop(self):
        sw_button = self.pig.callback(self.sw.gpio_sw, pigpio.RISING_EDGE, self.attachment)

        try:
            while True:
                sleep(0.01)
        except KeyboardInterrupt:
            self.pig.stop()


if __name__ == "__main__":
    led_sw = LED_SW()
    led_sw.loop()