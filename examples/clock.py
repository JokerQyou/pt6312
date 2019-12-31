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

from datetime import datetime

from pt6312.pt6312 import VFD
from pt6312.font_seg13 import * # FIXME

ucDotFlac = 0


def s(char):
    '''Char code lookup'''
    return SEG13_Char_Code[ord(char) - ord(' ')]


def main():
    vfd = VFD(8, 7, 1, hv_on=25)
    vfd.on()
    vfd.delay(200)

    while 1:
        now = datetime.now()
        # TODO Support colon mark
        now_str = now.strftime('%H%M%S ')
        buffer = [s(char) for char in now_str]
        vfd.update(buffer)
        vfd.delay(1000)


if __name__ == '__main__':
    main()
