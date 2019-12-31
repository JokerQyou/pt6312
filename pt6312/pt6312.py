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

from time import sleep

from gpiozero import OutputDevice as OP

from .constants import *


class VFD(object):

    def __init__(self, din, clk, stb, hv_on=17):
        # Hardcoded wires
        self.stb = OP(stb)
        self.din = OP(din)
        self.clk = OP(clk)

        self.hv = OP(hv_on)
        self.hv.on()

    def __repr__(self):
        return '<VFD device@{}>'.format(id(self))

    def send(self, data):
        for i in range(8):
            self.clk.off()
            if data & 0x01:
                self.din.on()
            else:
                self.din.off()

            data >>= 1
            self.clk.on()

    def send_stb(self):
        self.stb.on()
        self.stb.off()

    def init(self):
        self.send_stb()

        self.send(CMD2_CMD | WR_TO_DISPLAY_MODE_CMD)
        self.send_stb()

        self.send(CMD3_CMD)

        for i in range(8):
            self.send(0x00)
            self.send(0x00)

        self.send_stb()

        self.send(CMD1_CMD | PT6312_MODE)
        self.send_stb()

        self.send(CMD4_CMD | DISPLAY_ON | PT6312_LIGHT)
        self.send_stb()

    def display_all(self):
        self.send(CMD2_CMD | WR_TO_DISPLAY_MODE_CMD)
        self.send_stb()

        self.send(CMD3_CMD)

        for i in range(8):
            self.send(0xFF)
            self.send(0xFF)

        self.send_stb()

    def update(self, buffer):
        self.send(CMD2_CMD | WR_TO_DISPLAY_MODE_CMD)
        self.send_stb()

        self.send(CMD3_CMD)

        for i in range(7):
            self.send((buffer[i] >> 8) & 0x00FF)
            self.send(buffer[i] & 0x00FF)

        self.send_stb()

