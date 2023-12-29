from time import sleep

import pigpio

import Instruction as INST


class AQM0802:
    """AE-AQM0802+PCA9515 LCD(8x2)
    https://akizukidenshi.com/catalog/g/gK-11354/

      (AE-AQM0802)    [I2C Address: 0x3e]
     ┌─────────────┐  1: RST (NC) 
     │     LCD     │  2: GND
     │    (8x2)    │  3: LED (NC)
     │─────────────│  4: SCL
     └─│─│─│─│─│─│─┘  5: SDA
       1 2 3 4 5 6    6: 3V3
    """

    def __init__(self, debug=False):
        self.pi = pigpio.pi()
        self.h = None
        self.DEBUG = debug

    def open(self, i2c_bus=1, i2c_address=0x3e):
        self.h = self.pi.i2c_open(i2c_bus, i2c_address)
        if self.DEBUG: print(f"Handl# {self.h} opened.")

    def close(self):
        self.pi.i2c_close(self.h)
        if self.DEBUG: print(f"Hndle# {self.h} closed.")

    def display_initialize(self):
        if isinstance(self.h, type(None)):
            self.open()
        sleep(0.04)
        self.function_set(IS=False)
        self.function_set(IS=True)
        self.internal_OSC_frequency()
        self.contrast_set()
        self.power_icon_control_contrast_set()
        self.follower_control()
        sleep(0.3)
        self.function_set(IS=False)
        self.return_home()
        self.display_on_off(D=True,C=True,B=True)
        self.clear_display()
        sleep(0.5)
        if self.DEBUG: print("LCD initialized.")
    
    def clear_display(self):
        cmd = INST.CLEAR_DISPLAY
        if self.DEBUG: print(f"Clear Display: {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)

    def return_home(self):
        cmd = INST.RETURN_HOME
        if self.DEBUG: print(f"Return Home: {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)

    def entry_mode_set(self, ID=True, S=False):
        cmd = INST.ENTRY_MODE_SET
        cmd += INST.INCREMENT_MOVE_TO_RIGHT if ID else INST.DECREMENT_MOVE_TO_LEFT
        cmd += INST.SHIFT_OF_ENTIRE_DISPLAY_ON if S else INST.SHIFT_OF_ENTIRE_DISPLAY_OFF
        if self.DEBUG: print(f"Entry Mode Set: {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)

    def display_on_off(self, D=True, C=False, B=False):
        cmd = INST.DISPLAY_ON_OFF
        cmd += INST.ENTIRE_DISPLAY_ON if D else INST.ENTIRE_DISPLAY_OFF
        cmd += INST.CURSOR_VIEW_ON if C else INST.CURSOR_VIEW_OFF
        cmd += INST.CURSOR_BLINK_ON if B else INST.CURSOR_BLINK_OFF
        if self.DEBUG: print(f"Display ON/OFF: {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)

    def function_set(self, DL=True, N=True, DH=False, IS=False):
        cmd = INST.FUNCTION_SET
        cmd += INST.BIT8_BUS_MODE if DL else INST.BIT4_BUS_MODE
        cmd += INST.TOW_LINE_DISPLAY_MODE if N else INST.ONE_LINE_DISPLAY_MODE
        cmd += INST.DOUBLE_HEIGHT_FONT if DH else INST.NORMAL_HEIGHT_FONT
        cmd += INST.EXT_INST_TBL if IS else INST.NORMAL_INST_TBL
        if self.DEBUG: print(f"Function Set: {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)

    def set_ddram_address(self, pos=False):
        cmd = INST.SET_DDRAMADDRESS
        cmd += INST.DDRAM_ADDRESS2 if pos else INST.DDRAM_ADDRESS1
        if self.DEBUG: print(f"Set DDRAM address: {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)

    def write_data(self, data):
        hex_data = [ord(c) for c in list(data)]
        if self.DEBUG: print(f"Write Data(hex): {[hex(d) for d in hex_data]}")
        if self.DEBUG: print(f"Write Data(Chr): {[chr(d) for d in hex_data]}")
        rows = len(hex_data) // 8 + 1
        for row in range(rows):
            if row%2 == 0:
                self.set_ddram_address()
            else:
                self.set_ddram_address(pos=True)
            if self.DEBUG: print(f"{row}: {[chr(d) for d in hex_data[row*8:(row+1)*8]]}")
            for d in hex_data[row*8:(row+1)*8]:
                self.pi.i2c_write_byte_data(self.h, INST.DATA_WRITE, d)
            sleep(0.3)

    def cursor_shift(self, RL=True):
        cmd = INST.CURSOR_OR_DISPLAY_SHIFT
        cmd += INST.TO_RIGHT if RL else INST.TO_LEFT
        if self.DEBUG: print(f"Cursor Shift: {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)

    def display_shift(self, RL=True):
        cmd = INST.CURSOR_OR_DISPLAY_SHIFT
        cmd += INST.SCREEN_MOVE
        cmd += INST.TO_RIGHT if RL else INST.TO_LEFT
        if self.DEBUG: print(f"Screen Shift: {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)

    def power_icon_control_contrast_set(self):
        cmd = INST.POWER_ICON_CONTRAST_HIGH
        cmd += INST.ICON_DISPLAY_OFF
        cmd += INST.BOOSTER_CIRCUIT_ON
        cmd += INST.CONTRAST_HIGH
        if self.DEBUG: print(f"Power/Icon control/Contrast set(high): {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)

    def contrast_set(self):
        cmd = INST.CONTRAST_LOW
        if self.DEBUG: print(f"Contrast set(low): {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)
        
    def follower_control(self):
        cmd = INST.FOLLOWER_CONTROL
        cmd += INST.FOLLOWER_CIRCUIT_ON
        cmd += INST.FOLLOWER_AMPLIFIED_RAITO
        if self.DEBUG: print(f"Follower control: {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)
    
    def internal_OSC_frequency(self):
        cmd = INST.OSC_FREQUENCY
        cmd += INST.FREQUENCY_FOR_RF
        if self.DEBUG: print(f"Internal OSC frequency: {hex(cmd)}")
        self.pi.i2c_write_byte_data(self.h, INST.INSTRACTION, cmd)

if __name__ == "__main__":
    aqm0802 = AQM0802()
    aqm0802.open()
    aqm0802.display_initialize()
    aqm0802.function_set()
    aqm0802.display_on_off(C=True)
    aqm0802.write_data("Hello,World")
    aqm0802.display_shift()
    aqm0802.cursor_shift()
    sleep(1)
    aqm0802.clear_display()
    aqm0802.return_home()
    aqm0802.write_data("Good Bye!")
    sleep(2)
    aqm0802.display_on_off(D=False)
    aqm0802.close()
