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

from pt6312.pt6312 import VFD
from pt6312.font_seg13 import * # FIXME

VFD_Test = [
    SEG13_CHAR_V,
    SEG13_CHAR_F,
    SEG13_CHAR_D,
    SEG13_CHAR_T,
    SEG13_CHAR_E,
    SEG13_CHAR_S,
    SEG13_CHAR_T,
]
Dis_Buffer = [0] * 7

ucDotFlac = 0


def s(char):
    '''Char code lookup'''
    return SEG13_Char_Code[ord(char) - ord(' ')]

def main():
    vfd = VFD(10, 11, 8, hv_on=17)
    vfd.init()
    vfd.display_all()
    sleep(0.2)
    import pdb; pdb.set_trace()

    vfd.update(VFD_Test)
    sleep(0.2)

    Dis_Buffer = [
        s('H'),
        s('E'),
        s('L'),
        s('L'),
        s('O'),
        s('1'),
        s('1'),
    ]
    vfd.update(Dis_Buffer)


if __name__ == '__main__':
    main()
