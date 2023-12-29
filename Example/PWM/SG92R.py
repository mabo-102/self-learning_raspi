from time import sleep

import pigpio


class SG92R:
    """SG92R 
    https://akizukidenshi.com/catalog/g/gM-08914/

        (SG92R)
       ┌───────┐
       │       │   1: PWM (Orange)
       │       │   2: Vcc (Red)
       └─│─│─│─┘   3: GND (Brown)
         1 2 3
    """
    def __init__(self, gpio_pin=None, debug_mode: bool = False) -> None:
        self.pi = pigpio.pi()
        if isinstance(gpio_pin, type(None)):
            self.gpio_pin = 26
            print(f"GPIO#26 set.")
        else:
            self.gpio_pin = gpio_pin
        self.DEBUG = debug_mode
        self._initialize()

    def _initialize(self) -> None:
        self.pi.set_mode(self.gpio_pin, pigpio.OUTPUT)
        self.pi.write(self.gpio_pin, pigpio.HIGH)

    def start(self) -> None:
        self.pi.set_PWM_frequency(self.gpio_pin, 50)
        self.pi.set_PWM_range(self.gpio_pin, 1024)
        self.pi.set_PWM_dutycycle(self.gpio_pin, 25)
        self.pwm_status()
        sleep(0.5)
        self.pi.set_PWM_dutycycle(self.gpio_pin, 123)
        self.pwm_status()

    def stop(self) -> None:
        self.pi.set_PWM_dutycycle(self.gpio_pin, 0)

    def pwm_status(self) -> None:
        status = {}
        status["dutycycle"] = self.pi.get_PWM_dutycycle(self.gpio_pin)
        status["freauency"] = self.pi.get_PWM_frequency(self.gpio_pin)
        status["range"] = self.pi.get_PWM_range(self.gpio_pin)
        print(f"STATUS: {status}")
        


if __name__ == "__main__":
    sg92r = SG92R()
    while True:
        try:
            sg92r.start()
            sleep(1)
        except KeyboardInterrupt:
            sg92r.stop()
