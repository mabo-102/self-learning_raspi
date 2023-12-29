from time import sleep

import pigpio

from MCP320X import MCP320X
from LED import LED

class SPI_Main:
    """SPI
        SPI Sub (MCP3204)                   SPI Main (RasPi zero)
        ┌───────U───────┐                   ┌─────────────────┐
       CH0  (1)● (14) V_DD      <──────    (17) 3.3[V]        │
       CH1  (2)  (13) V_REF     <───┘                         │
       CH2  (3)  (12) AGND      ───────    (20) GND *         │
       CH3  (4)  (11) CLK       <──────    (23) GPIO11 (SCLK) │
        NC  (5)  (10) D_OUT     ──────>    (21) GPIO9 (MISO)  │
        NC  (6)  (9)  D_IN      <──────    (19) GPIO10 (MOSI) │
      DGND  (7)  (8)  CS/SHDN   <──────    (24) GPIO8 (CE0)   │
      │ └───────────────┘                   └─────────────────┘
      *                                     
    """
    def __init__(self,
                 clk: int = 11, mosi: int = 10, miso: int = 9, cs: int = 8,
                 ce: int = 0, speed: float = 10**6, vref: float = 3.3) -> None:
        # SPI Main (RasPi)
        self.CLK = clk
        self.MOSI = mosi
        self.MISO = miso
        self.CS = cs
        self.pig = pigpio.pi()
        self._spi_main_initialize()


    def _spi_main_initialize(self) -> None:
        self.pig.set_mode(self.CLK, pigpio.OUTPUT)
        self.pig.set_mode(self.MOSI, pigpio.OUTPUT)
        self.pig.set_mode(self.MISO, pigpio.INPUT)
        self.pig.set_mode(self.CS, pigpio.OUTPUT)


if __name__ == "__main__":
    spi_main = SPI_Main()
    spi_sub = MCP320X(debug_mode=True)
    CH = 0
    led = LED(25)
    while True:
        try:                    
            led.blink()
            digital_value = spi_sub.get_digital_value(CH)
            analog_value = spi_sub.to_convert_to_analog(digital_value)
            print(f"CH#{CH}: {digital_value} => {analog_value:.4f} [V]")
            sleep(0.5)
        except KeyboardInterrupt:
            spi_sub.cleanup()
            led.off()
            print(f"SPI communication is done.")
