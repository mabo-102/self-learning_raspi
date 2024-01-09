from time import sleep

import pigpio
from RPLCD.pigpio import CharLCD

class HD44780U:
    """HD44780U LCD(16x2)
    https://fab.cba.mit.edu/classes/863.06/11.13/44780.pdf
    (Amazon.co.jp: 1602A LCD)

            (HD44780U)           [4 bits Mode]
       1  2   15 16               1: VSS(GND)       11: D4 <- GPIO26
     ┌─│──│─//─│──│────────────┐  2: VDD(+5V)       12: D5 <- GPIO19
     │──────//─────────────────│  3: VD             13: D6 <- GPIO13
     │           LCD           │  4: RS <- GPIO21   14: D7 <- GPIO6
     │          (16x2)         │  5: RW(GND)        15: A (+5V)
     └──────//─────────────────┘  6: E <- GPIO16    16: K (GND)
    """
    def __init__(self, rs: int = 21, rw: int = None, e: int = 16, d4to7:list[int] = None) -> None:
        self.pi = pigpio.pi()
        self.rs = rs
        self.rw = rw
        self.e = e
        if d4to7 is None:
            self.d4to7 = [26, 19, 13, 6]
        else:
            self.d4to7 = d4to7
        self.lcd = CharLCD(
            self.pi,
            pin_rs=self.rs, pin_rw=self.rw, pin_e=self.e, pins_data=self.d4to7,
            cols=16, rows=2
        )

    def write(self, string: str = "Demo !") -> None:
        self.lcd.write_string(string)

    def clear(self) -> None:
        self.lcd.clear()

    def close(self) -> None:
        self.lcd.close(clear=True)

if __name__ == "__main__":
    LCD = HD44780U()
    LCD.write()
    sleep(3)
    LCD.clear()
    LCD.write("Hello, World !")
    sleep(3)
    LCD.close()
