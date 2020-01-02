# coding: utf-8
# Copyright (C) 2019 Joker Qyou
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from threading import Event

from gpiozero import OutputDevice as OP

from .constants import *
from .font_seg13 import SEG13_Char_Code as CHAR_TABLE, SEG13_CHAR_DP


class VFD(object):

    def __init__(self, din, clk, stb, hv_on=17):
        self.stb = OP(stb)
        self.din = OP(din)
        self.clk = OP(clk)
        self.hv = OP(hv_on)

        self.__sleep = Event()

        self.init()

    def __repr__(self):
        '''Object repr'''
        return '<VFD device@{} [DIN={},CLK={},STB={},HV_ON={}], currently {}>'.format(
            id(self),
            self.din.pin,
            self.clk.pin,
            self.stb.pin,
            self.hv.pin,
            'on' if self.hv.is_active else 'off',
        )

    def send(self, data):
        '''Send a single byte to the display controller.
        '''
        for i in range(8):
            self.clk.off()
            if data & 0x01:
                self.din.on()
            else:
                self.din.off()

            data >>= 1
            self.clk.on()

    def send_stb(self):
        '''Send a serial interface strobe signal to the display controller.
        This would create a falling edge on STB pin, and
        bytes sent after this signal will be processed as a command.
        '''
        self.stb.on()
        self.stb.off()

    def init(self):
        '''Init the display.
        '''
        self.send_stb()
        self.send(DATA_SET_CMD | DATA_WR | ADDR_INC | NORM_MODE)

        self.clear()
        self.set_mode(None)  # FIXME
        self.set_brightness(3)

    def clear(self):
        '''Clears display memory.
        This erases all digits from the display.
        '''
        self.send_stb()
        self.send(ADDR_SET_CMD)

        for i in range(8):
            self.send(0x00)
            self.send(0x00)

        self.send_stb()

    def set_mode(self, mode):
        '''Set display mode.
        '''
        # FIXME Currently only support 7 digits / 15 segments
        # NOTICE The center point of each digit cannot be lighted. It's not connected...
        self.send_stb()
        self.send(MODE_SET_CMD | PT6312_MODE)

        self.send_stb()

    def set_brightness(self, brightness):
        '''Set display brightness. Range [0,7]
        '''
        if brightness not in range(0, 8):
            raise ValueError('Invalid brightness value: {}. Must be in [0, 7]'.format(
                brightness
            ))
        self.send_stb()
        self.send(DSP_CTRL_CMD | DISPLAY_ON | brightness)

        self.send_stb()

    def on(self):
        '''Turn on the display.
        This only turns on the transformer, it does not touch the display memory.
        '''
        self.hv.on()

    def off(self):
        '''Turn off the display.
        This only turns off the transformer, it does not touch the display memory.
        '''
        self.hv.off()

    def delay(self, ms):
        '''Delay for given duration (in millisecond).
        '''
        self.__sleep.wait(ms / 1000.0)

    def display_all(self):
        '''Display all segments. Mainly for test.
        '''
        self.send(DATA_SET_CMD | DATA_WR | ADDR_INC | NORM_MODE)

        self.send_stb()
        self.send(ADDR_SET_CMD)

        for i in range(8):
            self.send(0xFF)
            self.send(0xFF)

        self.send_stb()

    def update(self, content):
        '''Update a slice / string into display memory.
        A more user-friendly version of .update_buffer(buffer)
        Notice:
          - `content` can be any thing with a length of 7.
          - if 3rd and 6th char in `content` is ':', these does not count.
        '''
        # Check for colon mark on 3rd and 6th char
        colon_left = colon_right = False
        base = ord(' ')
        if content[2] == ':':
            colon_left = True
            content = content[:2] + content[3:]
        if content[4] == ':':
            colon_right = True
            content = content[:4] + content[5:]

        if len(content) < 7:
            content += ' ' * (7 - len(content))
        else:
            raise ValueError('Can only display {} char at a time, but got {}'.format(
                7, len(content),
            ))

        # Convert to buffer data
        buffer = [CHAR_TABLE[ord(c) - base] for c in content]

        # Colon marks require special data bit
        if colon_left:
            buffer[2] |= SEG13_CHAR_DP
        else:
            buffer[2] &= ~SEG13_CHAR_DP

        if colon_right:
            buffer[4] |= SEG13_CHAR_DP
        else:
            buffer[4] &= ~SEG13_CHAR_DP

        # Send to display memory
        self.update_buffer(buffer)

    def update_buffer(self, buffer):
        '''Update a 7-digits buffer into display memory.
        '''
        self.send(DATA_SET_CMD | DATA_WR | ADDR_INC | NORM_MODE)
        self.send_stb()

        self.send(ADDR_SET_CMD)

        for i in range(7):
            self.send((buffer[i] >> 8) & 0x00FF)
            self.send(buffer[i] & 0x00FF)

        self.send_stb()

