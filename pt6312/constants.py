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
MODE_SET_CMD = 0x00
DISPLAY_4GRID_16SEGMENT_MODE = 0x00
DISPLAY_5GRID_16SEGMENT_MODE = 0x01
DISPLAY_6GRID_16SEGMENT_MODE = 0x02
DISPLAY_7GRID_15SEGMENT_MODE = 0x03
DISPLAY_8GRID_14SEGMENT_MODE = 0x04
DISPLAY_9GRID_13SEGMENT_MODE = 0x05
DISPLAY_10GRID_12SEGMENT_MODE = 0x06
DISPLAY_11GRID_11SEGMENT_MODE = 0x07

# COMMAND 2: DATA SETTING COMMANDS，设置数据从PT6312读或写
DATA_SET_CMD = 0x40
DATA_WR = 0x00  # Write to display
LED_WR = 0x01  # Write to LED port
KEY_RD = 0x02  # Read key data
SW_RD = 0x03  # Read SW data
ADDR_INC = 0x00  # Increment address after data has been written
ADDR_FIXED = 0x04  # Fixed address
NORM_MODE = 0x00  # Normal operation mode
TEST_MODE = 0x08  # Test mode

# COMMAND 3: ADDRESS SETTING COMMANDS，显示内存地址设置
ADDR_SET_CMD = 0xC0

# COMMAND 4: DISPLAY CONTROL COMMANDS，显示控制命令
DSP_CTRL_CMD = 0x80
DISPLAY_ON = 0x08
DISPLAY_OFF = 0x00

PT6312_MODE = DISPLAY_7GRID_15SEGMENT_MODE
