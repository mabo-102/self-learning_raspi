from time import sleep
import pigpio

from mcp3208 import mcp3208

SPICLK = 11
SPIMOSI = 10
SPIMISO = 9
SPICS = 8

SPI_CE = 0
SPI_SPEED = 1000000
VREF = 3.3
READ_CH = 0

LED = 25

pig = pigpio.pi()
pig.set_mode(SPICLK, pigpio.OUTPUT)
pig.set_mode(SPIMOSI, pigpio.OUTPUT)
pig.set_mode(SPIMISO, pigpio.INPUT)
pig.set_mode(SPICS, pigpio.OUTPUT)

try:
    adc = mcp3208(pig, SPI_CE, SPI_SPEED, VREF)
    while True:
        val = adc.get_value(READ_CH)
        print(val)
        if val%2 == 0:
            pig.write(LED, 1)
        else:
            pig.write(LED, 0)
        vol = adc.get_volt(val)
        print(f"Volt: {vol} [V]")
        sleep(1)
except KeyboardInterrupt:
    print("Loop End.")
#    pig.spi_close(adc.adc_h)
#    pig.stop()
finally:
    adc.cleanup()
    print("Done.")
