from time import sleep
import pigpio


class SW:
    def __init__(self, gpio=None) -> None:
        self.pig = pigpio.pi()
        if isinstance(gpio, type(None)):
            self.gpio_sw = 20
            print(f"Connect to GPIO#{self.gpio_sw}.")
        else:
            self.gpio_sw = gpio
        self.pig.set_mode(self.gpio_sw, pigpio.INPUT)
        self.pig.set_pull_up_down(self.gpio_sw, pigpio.PUD_DOWN)
    
    def status(self, gpio, level, tick):
        print(f"({tick}) GPIO# {gpio} => {level}")

    def loop(self):
        sw_button = self.pig.callback(self.gpio_sw, pigpio.RISING_EDGE, self.status)

        try:
            while True:
                sleep(0.01)
        except KeyboardInterrupt:
            self.pig.stop()


if __name__ == "__main__":
    sw = SW()
    sw.loop()
