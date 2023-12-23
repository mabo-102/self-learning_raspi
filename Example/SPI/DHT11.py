import sleep

import pigpio

class DHT11:
    def __init__(self, gpio=2) -> None:
        self.pig = pigpio.pi()
        self.gpio = gpio
    
    def sensor(self) -> float:
        self.pig.set_mode(self.gpio, pigpio.OUTPUT)
        self.pig.write(self.gpio, 1)
        sleep(0.05)
        self.pig.set_pull_up_down(self.gpio, pigpio.PUD_DOWN)
        self.pig.write(self.gpio, 0)
        sleep(0.02)

        self.pig.set_mode(self.gpio, pigpio.INPUT)
        self.pig.set_pull_up_down(self.gpio, pigpio.PUD_UP)
        data = self._collect_input()
        pu_len = self._parse_data_pu_len(data)

        if len(pu_len) != 40:
            raise Exception("PU_LEN", pu_len)
        bits = self._cal_bits(pu_len)
        the_bytes = self._bits2bytes(bits)
        checksum = self._cal_checksum(the_bytes)
        if the_bytes[4] != checksum:
            raise Exception("CHECKSUM", checksum)
        
        temperature = the_bytes[2]
        humidity = the_bytes[0]

        return (temperature, humidity)

    def _collect_input(self):
        uc = 0
        max_uc = 100
        last = -1
        data = []
        while True:
            cur = pigpio.input(self.gpio)
            data.append(cur)
            if last != cur:
                uc = 0
                last = cur
            else:
                uc += 1
                if uc > max_uc:
                    break
        
        return data
    
    def _pu_len(self, data):
        STATE_INIT_PULL_DOWN = 1
        STATE_INIT_PULL_UP = 2
        STATE_DATA_FIRST_PULL_DOWN = 3
        STATE_DATA_PULL_UP = 4
        STATE_DATA_PULL_DOWN = 5

        state = STATE_INIT_PULL_DOWN

        lengths = [] # will contain the lengths of data pull up periods
        current_length = 0 # will contain the length of the previous period

        for i in range(len(data)):

            current = data[i]
            current_length += 1

            if state == STATE_INIT_PULL_DOWN:
                if current == pigpio.PUD_DOWN:
                    # ok, we got the initial pull down
                    state = STATE_INIT_PULL_UP
                    continue
                else:
                    continue
            if state == STATE_INIT_PULL_UP:
                if current == pigpio.PUD_UP:
                    # ok, we got the initial pull up
                    state = STATE_DATA_FIRST_PULL_DOWN
                    continue
                else:
                    continue
            if state == STATE_DATA_FIRST_PULL_DOWN:
                if current == pigpio.PUD_DOWN:
                    # we have the initial pull down, the next will be the data pull up
                    state = STATE_DATA_PULL_UP
                    continue
                else:
                    continue
            if state == STATE_DATA_PULL_UP:
                if current == pigpio.PUD_DOWN:
                    # data pulled up, the length of this pull up will determine whether it is 0 or 1
                    current_length = 0
                    state = STATE_DATA_PULL_DOWN
                    continue
                else:
                    continue
            if state == STATE_DATA_PULL_DOWN:
                if current == pigpio.PUD_DOWN:
                    # pulled down, we store the length of the previous pull up period
                    lengths.append(current_length)
                    state = STATE_DATA_PULL_UP
                    continue
                else:
                    continue

        return lengths
    
    def _cal_bits(self, pu_len):
        # find shortest and longest period
        shortest_pull_up = 1000
        longest_pull_up = 0

        for i in range(0, len(pu_len)):
            length = pu_len[i]
            if length < shortest_pull_up:
                shortest_pull_up = length
            if length > longest_pull_up:
                longest_pull_up = length

        # use the halfway to determine whether the period it is long or short
        halfway = shortest_pull_up + (longest_pull_up - shortest_pull_up) / 2
        bits = []

        for i in range(0, len(pu_len)):
            bit = False
            if pu_len[i] > halfway:
                bit = True
            bits.append(bit)

        return bits
    
    def _bits2bytes(self, bits):
        the_bytes = []
        byte = 0

        for i in range(0, len(bits)):
            byte = byte << 1
            if (bits[i]):
                byte = byte | 1
            else:
                byte = byte | 0
            if ((i + 1) % 8 == 0):
                the_bytes.append(byte)
                byte = 0

        return the_bytes

    def _cal_checksum(self, the_bytes):
        return the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3] & 255
