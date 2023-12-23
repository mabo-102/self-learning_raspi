# Registor
"""
control byte: [Co|RS|0|0|0|0|0|0]
Co: 0 -> Last Data
RS: 0 -> Instruction Write Operation
    1 -> Data Write Operation
"""
INSTRACTION = 0x00
DATA_WRITE = 0x40


# Instruction Table

# Clear Display
CLEAR_DISPLAY = 0x01

# return Home
RETURN_HOME = 0x02

# Entry Mode Set
ENTRY_MODE_SET = 0x04

INCREMENT_MOVE_TO_RIGHT = 0x02
DECREMENT_MOVE_TO_LEFT = 0x00

SHIFT_OF_ENTIRE_DISPLAY_ON = 0x01
SHIFT_OF_ENTIRE_DISPLAY_OFF = 0x00

# Display ON/OFF
DISPLAY_ON_OFF = 0x08

ENTIRE_DISPLAY_ON = 0x04
ENTIRE_DISPLAY_OFF = 0x00
CURSOR_VIEW_ON = 0x02
CURSOR_VIEW_OFF = 0x00
CURSOR_BLINK_ON = 0x01
CURSOR_BLINK_OFF = 0x00

# Function Set
FUNCTION_SET = 0x20

BIT8_BUS_MODE = 0x10
BIT4_BUS_MODE = 0x00
TOW_LINE_DISPLAY_MODE = 0x08
ONE_LINE_DISPLAY_MODE = 0x00
DOUBLE_HEIGHT_FONT = 0x04
NORMAL_HEIGHT_FONT = 0x00
EXT_INST_TBL = 0x01
NORMAL_INST_TBL = 0x00

# Set DDRAM address
SET_DDRAMADDRESS = 0x80

DDRAM_ADDRESS1 = 0x00
DDRAM_ADDRESS2 = 0x40

# Cursor or Display Shift
CURSOR_OR_DISPLAY_SHIFT = 0x10

SCREEN_MOVE = 0x08
CURSOR_MOVE = 0x00
TO_RIGHT = 0x04
TO_LEFT = 0x00

# Set CGRAM Adress
SET_CGRAM_ADDRESS = 0x40

# Internal OSC frequency
OSC_FREQUENCY = 0x10

FREQUENCY_FOR_RF = 0x04

# Power/ICON control/Contrast set(high byte)
POWER_ICON_CONTRAST_HIGH = 0x50

ICON_DISPLAY_ON = 0x08
ICON_DISPLAY_OFF = 0x00
BOOSTER_CIRCUIT_ON = 0x04
BOOSTER_CIRCUIT_OFF = 0x00
CONTRAST_HIGH = 0x02

# Follower control
FOLLOWER_CONTROL = 0x60

FOLLOWER_CIRCUIT_ON = 0x08
FOLLOWER_AMPLIFIED_RAITO = 0x04

# Contrast set(low byte)
CONTRAST_LOW = 0x70