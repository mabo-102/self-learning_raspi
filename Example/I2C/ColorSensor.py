from time import sleep

import pigpio


class ColorSensor:
    """AE-S11059: I2C Digital Color Sensor
    https://akizukidenshi.com/catalog/g/gK-08316/

      (AE-S11059)    [I2C Address: 0x2a]
     ┌────────────┐  1: 3V3 (5.0[V] NG!) 
     │    ┌──┐    │  2: SDA
     │    │  │    │  3: SCL
     │    └──┘    │  4: GND
     └─│──│──│──│─┘
       1  2  3  4
    """
    def __init__(self, debug_mode=False):
        self.pi = pigpio.pi()
        self.h = None
        self.measurement_time = 3.0
        self.DEBUG = debug_mode

    def open(self, i2c_bus=1, i2c_address=0x2a):
        self.h = self.pi.i2c_open(i2c_bus, i2c_address)
        if self.DEBUG: print(f"Handl# {self.h} opened.")

    def close(self):
        self.pi.i2c_close(self.h)
        if self.DEBUG: print(f"Hndle# {self.h} closed.")

    def _poweron_reset(self) -> None:
        cmd = 0x80
        self.pi.i2c_write_byte_data(self.h, 0x00, cmd)

    def _initialize(self) -> None:
        cmd = 0x04
        self.pi.i2c_write_byte_data(self.h, 0x00, cmd)

    def adc_reset_on_off(self, reset_mode: bool = True):
        pass

    def sleep_on_off(self, sleep_mode: bool = True):
        pass

    def set_manual_timing(self, Tint: int = 0, timing_num: int = 0xc30):
        TINT_MASK = 0x03
        Tint &= TINT_MASK
        cmd = 0xE0
        cmd += Tint
        self.pi.i2c_write_byte_data(self.h, 0x00, cmd)
        if self.DEBUG: print(f"Tint: {Tint}, TIMING_NUM: {timing_num}")
        self.pi.i2c_write_word_data(self.h, 0x01, timing_num)

    def begin_measurement(self):
        sleep(self.measurement_time)
        print(f"{self.measurement_time*10**3}[ms] Measuring...")

    def end_measurement(self) -> list:
        result_data = []
        BASE_ADDR = 0x03

        for i in range(8):
            reg_addr = BASE_ADDR + i
            d = self.pi.i2c_read_byte_data(self.h, reg_addr)
            if i%2 == 0:
                d_high = d<<8
            else:
                result_data.append(d_high | d)

        return result_data
    
    def measurement_result(self, result_data):
        print(f"R: {result_data[0]}, G: {result_data[1]}, B: {result_data[2]}, IR: {result_data[3]}")


if __name__ == "__main__":
    cs = ColorSensor(debug_mode=True)
    cs.open()
    cs._poweron_reset()
    cs._initialize()
    cs.set_manual_timing(Tint=3)
    cs.begin_measurement()
    result_data = cs.end_measurement()
    print(result_data)
    cs.measurement_result(result_data)
    cs.close()
