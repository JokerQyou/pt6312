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

# COMMAND 1: DISPLAY MODE SETTING COMMANDS，显示模式设置
CMD1_CMD = 0x00
DISPLAY_4GRID_16SEGMENT_MODE = 0x00
DISPLAY_5GRID_16SEGMENT_MODE = 0x01
DISPLAY_6GRID_16SEGMENT_MODE = 0x02
DISPLAY_7GRID_15SEGMENT_MODE = 0x03
DISPLAY_8GRID_14SEGMENT_MODE = 0x04
DISPLAY_9GRID_13SEGMENT_MODE = 0x05
DISPLAY_10GRID_12SEGMENT_MODE = 0x06
DISPLAY_11GRID_11SEGMENT_MODE = 0x07

# COMMAND 2: DATA SETTING COMMANDS，设置数据从PT6312读或写
CMD2_CMD = 0x40
WR_TO_DISPLAY_MODE_CMD = 0x00
WR_TO_LED_PORT_CMD = 0x01
RD_KEY_DATA_CMD = 0x02
RD_SW_DATA_CMD = 0x03
FIXED_ADDRESS_CMD = 0x04  

# COMMAND 3: ADDRESS SETTING COMMANDS，显示内存地址设置
CMD3_CMD = 0xC0

# COMMAND 4: DISPLAY CONTROL COMMANDS，显示控制命令
CMD4_CMD = 0x80
DISPLAY_ON = 0x08
DISPLAY_OFF = 0x00

PT6312_MODE = DISPLAY_7GRID_15SEGMENT_MODE
