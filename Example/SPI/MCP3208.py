import pigpio

class MCP3208:
    """MCP3208
     ┌───────U───────┐
    CH0  (1)● (16) V_DD: 2.7 - 5.5[V]
    CH1  (2)  (15) V_REF
    CH2  (3)  (14) AGND: Analog side DND
    CH3  (4)  (13) CLK
    CH4  (5)  (12) D_OUT: MISO
    CH5  (6)  (11) D_IN: MOSI
    CH6  (7)  (10) CS/SHDN
    CH7  (8)  (9)  DGND
     └───────────────┘
    """
    def __init__(self, gpio, ss, speed, vref):
        self.ss = ss
        self.speed = speed
        self.vref = vref
        self.pi = gpio
        
        self.adc_h = self.pi.spi_open(self.ss, self.speed, 0)
        
    def get_value(self, ch):
        cmd_h = 0b110 | (ch >> 2)
        cmd_l = (ch & 0b11) << 6
        (c, raw) = self.pi.spi_xfer(self.adc_h, [cmd_h, cmd_l, 0])
        value =  (raw[1] & 0x0f) <<8 | raw[2]
        return value

    def get_volt(self, value):
        return value * self.vref / float(4095)

    def cleanup(self):
        self.pi.spi_close(self.adc_h)
