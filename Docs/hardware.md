# RaspberryPi Hardware

- [Raspberry Pi hardware](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)


## RaspberryPi Zero

```sh:
$ pinout
.-------------------------.
| oooooooooooooooooooo J8 |
| 1ooooooooooooooooooo   |c
---+       +---+ PiZero W|s
 sd|       |SoC|   V1.1  |i
---+|hdmi| +---+  usb pwr |
`---|    |--------| |-| |-'

Revision           : 9000c1
SoC                : BCM2835
RAM                : 512MB
Storage            : MicroSD
USB ports          : 1 (of which 0 USB3)
Ethernet ports     : 0 (0Mbps max. speed)
Wi-fi              : True
Bluetooth          : True
Camera ports (CSI) : 1
Display ports (DSI): 0

J8:
   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

For further information, please refer to https://pinout.xyz/
```

```sh:
$ raspi-gpio get
BANK0 (GPIO 0 to 27):
GPIO 0: level=1 fsel=0 func=INPUT
GPIO 1: level=1 fsel=0 func=INPUT
GPIO 2: level=1 fsel=0 func=INPUT
GPIO 3: level=1 fsel=0 func=INPUT
GPIO 4: level=1 fsel=0 func=INPUT
GPIO 5: level=1 fsel=0 func=INPUT
GPIO 6: level=1 fsel=0 func=INPUT
GPIO 7: level=1 fsel=0 func=INPUT
GPIO 8: level=1 fsel=0 func=INPUT
GPIO 9: level=0 fsel=0 func=INPUT
GPIO 10: level=0 fsel=0 func=INPUT
GPIO 11: level=0 fsel=0 func=INPUT
GPIO 12: level=0 fsel=0 func=INPUT
GPIO 13: level=0 fsel=0 func=INPUT
GPIO 14: level=0 fsel=0 func=INPUT
GPIO 15: level=1 fsel=0 func=INPUT
GPIO 16: level=0 fsel=0 func=INPUT
GPIO 17: level=0 fsel=0 func=INPUT
GPIO 18: level=0 fsel=0 func=INPUT
GPIO 19: level=0 fsel=0 func=INPUT
GPIO 20: level=0 fsel=0 func=INPUT
GPIO 21: level=0 fsel=0 func=INPUT
GPIO 22: level=0 fsel=0 func=INPUT
GPIO 23: level=0 fsel=0 func=INPUT
GPIO 24: level=0 fsel=0 func=INPUT
GPIO 25: level=0 fsel=0 func=INPUT
GPIO 26: level=0 fsel=0 func=INPUT
GPIO 27: level=0 fsel=0 func=INPUT
BANK1 (GPIO 28 to 45):
GPIO 28: level=1 fsel=0 func=INPUT
GPIO 29: level=1 fsel=0 func=INPUT
GPIO 30: level=0 fsel=7 alt=3 func=CTS0
GPIO 31: level=0 fsel=7 alt=3 func=RTS0
GPIO 32: level=1 fsel=7 alt=3 func=TXD0
GPIO 33: level=1 fsel=7 alt=3 func=RXD0
GPIO 34: level=0 fsel=7 alt=3 func=SD1_CLK
GPIO 35: level=1 fsel=7 alt=3 func=SD1_CMD
GPIO 36: level=1 fsel=7 alt=3 func=SD1_DAT0
GPIO 37: level=1 fsel=7 alt=3 func=SD1_DAT1
GPIO 38: level=1 fsel=7 alt=3 func=SD1_DAT2
GPIO 39: level=1 fsel=7 alt=3 func=SD1_DAT3
GPIO 40: level=0 fsel=1 func=OUTPUT
GPIO 41: level=1 fsel=1 func=OUTPUT
GPIO 42: level=0 fsel=0 func=INPUT
GPIO 43: level=1 fsel=4 alt=0 func=GPCLK2
GPIO 44: level=0 fsel=1 func=OUTPUT
GPIO 45: level=1 fsel=1 func=OUTPUT
BANK2 (GPIO 46 to 53):
GPIO 46: level=1 fsel=0 func=INPUT
GPIO 47: level=0 fsel=1 func=OUTPUT
GPIO 48: level=0 fsel=4 alt=0 func=SD0_CLK
GPIO 49: level=1 fsel=4 alt=0 func=SD0_CMD
GPIO 50: level=1 fsel=4 alt=0 func=SD0_DAT0
GPIO 51: level=1 fsel=4 alt=0 func=SD0_DAT1
GPIO 52: level=1 fsel=4 alt=0 func=SD0_DAT2
GPIO 53: level=1 fsel=4 alt=0 func=SD0_DAT3
```

## 電子工作

- [秋月電子](https://akizukidenshi.com/catalog/)