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

from pt6312 import VFD


def main():
    vfd = VFD(8, 7, 1, hv_on=25)
    vfd.on()
    vfd.delay(200)

    while 1:
        now = datetime.now()
        vfd.update(now.strftime('%H:%M:%S'))
        vfd.delay(1000)


if __name__ == '__main__':
    main()
