import pigpio

class MCP320X:
    """https://akizukidenshi.com/download/MCP3208.pdf

     SPI Sub (MCP3208)             SPI Sub (MCP3204)
     ┌───────U───────┐             ┌───────U───────┐ 
    CH0  (1)● (16) V_DD           CH0  (1)● (14) V_DD
    CH1  (2)  (15) V_REF          CH1  (2)  (13) V_REF
    CH2  (3)  (14) AGND           CH2  (3)  (12) AGND         
    CH3  (4)  (13) CLK            CH3  (4)  (11) CLK 
    CH4  (5)  (12) D_OUT           NC  (5)  (10) D_OUT  
    CH5  (6)  (11) D_IN            NC  (6)  (9)  D_IN 
    CH6  (7)  (10) CS/SHDN       DGND  (7)  (8)  CS/SHDN   
    CH7  (8)  (9)  DGND            └───────────────┘
     └───────────────┘
    """
    def __init__(self, ce: int = 0, speed: float = 100*10**3, vref: float = 3.3, debug_mode=False) -> None:
        self.CE = ce
        self.SPEED = speed
        self.VREF = vref
        self.pig = pigpio.pi()
        self.flags = 0
        self.DEBUG = debug_mode

        self.adc_h = self.pig.spi_open(self.CE, self.SPEED, self.flags)
        
    def get_digital_value(self, ch):
        # cmd_h: Dummy(5bit) is "0" + StartBit "1" + Single Mode "1" + D2
        #    D2: CH0(0b"0"00) - 7(0b"1"11) = ch >> 2
        cmd_h = 0b110 | (ch >> 2)
        if self.DEBUG:
            print(f"CMD_H: {cmd_h}, {format(cmd_h, '08b')}")

        # cmd_l: D1 + D0 + Dummy(6bit) is "0"
        # D1,D0: CH0(0b0"00") - 7(0b1"11") = ch & 0b11
        cmd_l = (ch & 0b11) << 6
        if self.DEBUG:
            print(f"CMD_L: {cmd_l}, {format(cmd_l, '08b')}")

        dummy = 0b00000000

        (c, raw) = self.pig.spi_xfer(self.adc_h, [cmd_h, cmd_l, dummy])
        if self.DEBUG:
            print(f"RECEVI RAW DATA({c} bytes): {raw}")

        # receive data: 
        # 1st:  [?(8bit)]
        # 2nd:  [?(3bit) + 0(Null) + B11-B8(4bit)]
        # last: [B7-B0(8bit)]
        digital_value =  (raw[1] & 0x0f) <<8 | raw[2]
        if self.DEBUG:
            print(f"DIGITAL VALUE: {digital_value}")
        return digital_value


    def to_convert_to_analog(self, digital_value):
        return digital_value * self.VREF / float(4096)


    def cleanup(self):
        self.pig.spi_close(self.adc_h)
