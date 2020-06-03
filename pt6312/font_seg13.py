# coding: utf8
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

# Just a placeholder for an empty cell in the characters definition table
_______ = 0

# Segments definition
# 高电平点亮，移植时需要根据实际修改
SEG13_A = 0x0200    # 码段A显示
SEG13_B = 0x1000    # 码段B显示
SEG13_C = 0x0001    # 码段C显示
SEG13_D = 0x0020    # 码段D显示
SEG13_E = 0x0002    # 码段E显示
SEG13_F = 0x2000    # 码段F显示
SEG13_G = 0x8000    # 码段G显示
SEG13_H = 0x0400    # 码段H显示
SEG13_I = 0x0010    # 码段I显示
SEG13_J = 0x0800    # 码段J显示
SEG13_K = 0x0008    # 码段K显示
SEG13_M = 0x4000    # 码段M显示
SEG13_N = 0x0004    # 码段N显示
SEG13_DP = 0x0100   # 码段DP显示
SEG13_BLK = 0x0000  # 无显


# Characters definition
# 共阴型数码管，码段高电平公共端低电平点亮
SEG13_CHAR_SP      = (_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______)  # (space)
SEG13_CHAR_EXCLA   = (_______|_______|_______|SEG13_D|_______|_______|_______|_______|SEG13_I|_______|_______|_______|_______)  # !
SEG13_CHAR_DOUBL   = (_______|SEG13_B|_______|_______|_______|_______|_______|_______|_______|SEG13_J|_______|_______|_______)  # "
SEG13_CHAR_NUMBE   = (_______|SEG13_B|SEG13_C|SEG13_D|_______|_______|SEG13_G|_______|SEG13_I|_______|_______|SEG13_M|_______)  # #
SEG13_CHAR_DOLLA   = (SEG13_A|_______|SEG13_C|SEG13_D|_______|SEG13_F|SEG13_G|_______|SEG13_I|_______|_______|SEG13_M|_______)  # $
SEG13_CHAR_PERCE   = (_______|_______|SEG13_C|_______|_______|SEG13_F|SEG13_G|SEG13_H|_______|SEG13_J|SEG13_K|SEG13_M|SEG13_N)  # %
SEG13_CHAR_AMPER   = (SEG13_A|_______|_______|SEG13_D|SEG13_E|_______|SEG13_G|SEG13_H|_______|SEG13_J|SEG13_K|_______|_______)  # &
SEG13_CHAR_SINGL   = (_______|_______|_______|_______|_______|_______|_______|_______|_______|SEG13_J|_______|_______|_______)  # '
SEG13_CHAR_LEFTP   = (_______|_______|_______|_______|_______|_______|_______|_______|_______|SEG13_J|SEG13_K|_______|_______)  # (
SEG13_CHAR_RIGHP   = (_______|_______|_______|_______|_______|_______|_______|SEG13_H|_______|_______|_______|_______|SEG13_N)  # )
SEG13_CHAR_ASTER   = (_______|_______|_______|_______|_______|_______|SEG13_G|SEG13_H|SEG13_I|SEG13_J|SEG13_K|SEG13_M|SEG13_N)  # *
SEG13_CHAR_PLUS    = (_______|_______|_______|_______|_______|_______|SEG13_G|_______|SEG13_I|_______|_______|SEG13_M|_______)  # +
SEG13_CHAR_COMMA   = (_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|SEG13_N)  # ,
SEG13_CHAR_DASH    = (_______|_______|_______|_______|_______|_______|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # -
SEG13_CHAR_DOT     = (_______|_______|SEG13_C|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______)  # .
SEG13_CHAR_FSLAS   = (_______|_______|_______|_______|_______|_______|_______|_______|_______|SEG13_J|_______|_______|SEG13_N)  # /
SEG13_CHAR_0       = (SEG13_A|SEG13_B|SEG13_C|SEG13_D|SEG13_E|SEG13_F|_______|_______|_______|_______|_______|_______|_______)  # 0
SEG13_CHAR_1       = (_______|SEG13_B|SEG13_C|_______|_______|_______|_______|_______|_______|SEG13_J|_______|_______|_______)  # 1
SEG13_CHAR_2       = (SEG13_A|SEG13_B|_______|SEG13_D|SEG13_E|_______|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # 2
SEG13_CHAR_3       = (SEG13_A|SEG13_B|SEG13_C|SEG13_D|_______|_______|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # 3
SEG13_CHAR_4       = (_______|SEG13_B|SEG13_C|_______|_______|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # 4
SEG13_CHAR_5       = (SEG13_A|_______|SEG13_C|SEG13_D|_______|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # 5
SEG13_CHAR_6       = (SEG13_A|_______|SEG13_C|SEG13_D|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # 6
SEG13_CHAR_7       = (SEG13_A|SEG13_B|SEG13_C|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______)  # 7
SEG13_CHAR_8       = (SEG13_A|SEG13_B|SEG13_C|SEG13_D|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # 8
SEG13_CHAR_9       = (SEG13_A|SEG13_B|SEG13_C|SEG13_D|_______|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # 9
SEG13_CHAR_COLON   = (SEG13_A|_______|_______|SEG13_D|_______|_______|_______|_______|_______|_______|_______|_______|_______)  # :
SEG13_CHAR_SEMIC   = (_______|SEG13_B|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|SEG13_N)  # ;
SEG13_CHAR_LESST   = (_______|_______|_______|_______|_______|_______|SEG13_G|_______|_______|SEG13_J|SEG13_K|_______|_______)  # <
SEG13_CHAR_EQUAL   = (_______|_______|_______|SEG13_D|_______|_______|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # =
SEG13_CHAR_MORET   = (_______|_______|_______|_______|_______|_______|_______|SEG13_H|_______|_______|_______|SEG13_M|SEG13_N)  # >
SEG13_CHAR_QUEST   = (SEG13_A|SEG13_B|_______|_______|SEG13_E|_______|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # ?
SEG13_CHAR_AT      = (SEG13_A|SEG13_B|_______|SEG13_D|SEG13_E|SEG13_F|_______|_______|_______|SEG13_J|_______|SEG13_M|_______)  # @
SEG13_CHAR_A       = (SEG13_A|SEG13_B|SEG13_C|_______|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # A
SEG13_CHAR_B       = (SEG13_A|SEG13_B|SEG13_C|SEG13_D|_______|_______|_______|_______|SEG13_I|_______|_______|SEG13_M|_______)  # B
SEG13_CHAR_C       = (SEG13_A|_______|_______|SEG13_D|SEG13_E|SEG13_F|_______|_______|_______|_______|_______|_______|_______)  # C
SEG13_CHAR_D       = (SEG13_A|SEG13_B|SEG13_C|SEG13_D|_______|_______|_______|_______|SEG13_I|_______|_______|_______|_______)  # D
SEG13_CHAR_E       = (SEG13_A|_______|_______|SEG13_D|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # E
SEG13_CHAR_F       = (SEG13_A|_______|_______|_______|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # F
SEG13_CHAR_G       = (SEG13_A|_______|SEG13_C|SEG13_D|SEG13_E|SEG13_F|_______|_______|_______|_______|_______|SEG13_M|_______)  # G
SEG13_CHAR_H       = (_______|SEG13_B|SEG13_C|_______|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # H
SEG13_CHAR_I       = (SEG13_A|_______|_______|SEG13_D|_______|_______|_______|_______|SEG13_I|_______|_______|_______|_______)  # I
SEG13_CHAR_J       = (_______|SEG13_B|SEG13_C|SEG13_D|SEG13_E|_______|_______|_______|_______|_______|_______|_______|_______)  # J
SEG13_CHAR_K       = (_______|_______|_______|_______|SEG13_E|SEG13_F|SEG13_G|_______|_______|SEG13_J|SEG13_K|_______|_______)  # K
SEG13_CHAR_L       = (_______|_______|_______|SEG13_D|SEG13_E|SEG13_F|_______|_______|_______|_______|_______|_______|_______)  # L
SEG13_CHAR_M       = (_______|SEG13_B|SEG13_C|_______|SEG13_E|SEG13_F|_______|SEG13_H|_______|SEG13_J|_______|_______|_______)  # M
SEG13_CHAR_N       = (_______|SEG13_B|SEG13_C|_______|SEG13_E|SEG13_F|_______|SEG13_H|_______|_______|SEG13_K|_______|_______)  # N
SEG13_CHAR_O       = (SEG13_A|SEG13_B|SEG13_C|SEG13_D|SEG13_E|SEG13_F|_______|_______|_______|_______|_______|_______|_______)  # O
SEG13_CHAR_P       = (SEG13_A|SEG13_B|_______|_______|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # P
SEG13_CHAR_Q       = (SEG13_A|SEG13_B|SEG13_C|SEG13_D|SEG13_E|SEG13_F|_______|_______|_______|_______|SEG13_K|_______|_______)  # Q
SEG13_CHAR_R       = (SEG13_A|SEG13_B|_______|_______|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|SEG13_K|SEG13_M|_______)  # R
SEG13_CHAR_S       = (SEG13_A|_______|_______|SEG13_D|_______|SEG13_F|SEG13_G|_______|_______|_______|SEG13_K|_______|_______)  # S
SEG13_CHAR_T       = (SEG13_A|_______|_______|_______|_______|_______|_______|_______|SEG13_I|_______|_______|_______|_______)  # T
SEG13_CHAR_U       = (_______|SEG13_B|SEG13_C|SEG13_D|SEG13_E|SEG13_F|_______|_______|_______|_______|_______|_______|_______)  # U
SEG13_CHAR_V       = (_______|_______|_______|_______|SEG13_E|SEG13_F|_______|_______|_______|SEG13_J|_______|_______|SEG13_N)  # V
SEG13_CHAR_W       = (_______|SEG13_B|SEG13_C|_______|SEG13_E|SEG13_F|_______|_______|_______|_______|SEG13_K|_______|SEG13_N)  # W
SEG13_CHAR_X       = (_______|_______|_______|_______|_______|_______|_______|SEG13_H|_______|SEG13_J|SEG13_K|_______|SEG13_N)  # X
SEG13_CHAR_Y       = (_______|SEG13_B|SEG13_C|SEG13_D|_______|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # Y
SEG13_CHAR_Z       = (SEG13_A|_______|_______|SEG13_D|_______|_______|_______|_______|_______|SEG13_J|_______|_______|SEG13_N)  # Z
SEG13_CHAR_LOBRA   = (SEG13_A|_______|_______|SEG13_D|SEG13_E|SEG13_F|_______|_______|_______|_______|_______|_______|_______)  # [
SEG13_CHAR_BSLAS   = (_______|_______|_______|_______|_______|_______|_______|SEG13_H|_______|_______|SEG13_K|_______|_______)  # \
SEG13_CHAR_ROBRA   = (SEG13_A|SEG13_B|SEG13_C|SEG13_D|_______|_______|_______|_______|_______|_______|_______|_______|_______)  # ]
SEG13_CHAR_CARET   = (_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|SEG13_K|_______|SEG13_N)  # ^
SEG13_CHAR_USCOR   = (_______|_______|_______|SEG13_D|_______|_______|_______|_______|_______|_______|_______|_______|_______)  # _
SEG13_CHAR_BQUOT   = (_______|_______|_______|_______|_______|_______|_______|SEG13_H|_______|_______|_______|_______|_______)  # `
SEG13_CHAR_a       = (_______|_______|_______|SEG13_D|SEG13_E|_______|SEG13_G|_______|_______|_______|_______|_______|SEG13_N)  # a
SEG13_CHAR_b       = (_______|_______|_______|SEG13_D|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|SEG13_K|_______|_______)  # b
SEG13_CHAR_c       = (_______|_______|_______|SEG13_D|SEG13_E|_______|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # c
SEG13_CHAR_d       = (_______|SEG13_B|SEG13_C|SEG13_D|_______|_______|_______|_______|_______|_______|_______|SEG13_M|SEG13_N)  # d
SEG13_CHAR_e       = (_______|_______|_______|SEG13_D|SEG13_E|_______|SEG13_G|_______|_______|_______|_______|SEG13_M|SEG13_N)  # e
SEG13_CHAR_f       = (_______|SEG13_B|_______|_______|_______|_______|SEG13_G|_______|_______|SEG13_J|_______|SEG13_M|SEG13_N)  # f
SEG13_CHAR_g       = (_______|SEG13_B|SEG13_C|SEG13_D|_______|_______|_______|_______|_______|SEG13_J|_______|SEG13_M|_______)  # g
SEG13_CHAR_h       = (_______|_______|_______|_______|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|SEG13_K|_______|_______)  # h
SEG13_CHAR_i       = (_______|_______|_______|_______|_______|_______|_______|_______|SEG13_I|_______|_______|_______|_______)  # i
SEG13_CHAR_j       = (_______|_______|_______|_______|SEG13_E|_______|_______|_______|_______|SEG13_J|_______|_______|SEG13_N)  # j
SEG13_CHAR_k       = (_______|_______|_______|_______|_______|_______|_______|_______|SEG13_I|SEG13_J|SEG13_K|_______|_______)  # k
SEG13_CHAR_l       = (_______|_______|_______|_______|SEG13_E|SEG13_F|_______|_______|_______|_______|_______|_______|_______)  # l
SEG13_CHAR_m       = (_______|_______|SEG13_C|_______|SEG13_E|_______|SEG13_G|_______|SEG13_I|_______|_______|SEG13_M|_______)  # m
SEG13_CHAR_n       = (_______|_______|SEG13_C|_______|SEG13_E|_______|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # n
SEG13_CHAR_o       = (_______|_______|SEG13_C|SEG13_D|SEG13_E|_______|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # o
SEG13_CHAR_p       = (_______|_______|_______|_______|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|_______|_______|_______)  # p
SEG13_CHAR_q       = (_______|SEG13_B|SEG13_C|_______|_______|_______|_______|_______|_______|SEG13_J|_______|SEG13_M|_______)  # q
SEG13_CHAR_r       = (_______|_______|_______|_______|SEG13_E|_______|SEG13_G|_______|_______|_______|_______|_______|_______)  # r
SEG13_CHAR_s       = (_______|_______|_______|SEG13_D|_______|_______|_______|_______|_______|_______|SEG13_K|SEG13_M|_______)  # s
SEG13_CHAR_t       = (_______|_______|_______|SEG13_D|SEG13_E|SEG13_F|SEG13_G|_______|_______|_______|_______|_______|_______)  # t
SEG13_CHAR_u       = (_______|_______|SEG13_C|SEG13_D|SEG13_E|_______|_______|_______|_______|_______|_______|_______|_______)  # u
SEG13_CHAR_v       = (_______|_______|_______|_______|SEG13_E|_______|_______|_______|_______|_______|_______|_______|SEG13_N)  # v
SEG13_CHAR_w       = (_______|_______|SEG13_C|_______|SEG13_E|_______|_______|_______|_______|_______|SEG13_K|_______|SEG13_N)  # w
SEG13_CHAR_x       = (_______|_______|_______|_______|_______|_______|_______|SEG13_H|_______|SEG13_J|SEG13_K|_______|SEG13_N)  # x
SEG13_CHAR_y       = (_______|SEG13_B|SEG13_C|SEG13_D|_______|_______|_______|SEG13_H|_______|_______|_______|SEG13_M|_______)  # y
SEG13_CHAR_z       = (_______|_______|_______|SEG13_D|_______|_______|SEG13_G|_______|_______|_______|_______|_______|SEG13_N)  # z
SEG13_CHAR_LBRAC   = (SEG13_A|_______|_______|SEG13_D|_______|_______|SEG13_G|SEG13_H|_______|_______|_______|_______|SEG13_N)  # {
SEG13_CHAR_VERTI   = (_______|_______|_______|_______|_______|_______|_______|_______|SEG13_I|_______|_______|_______|_______)  # |
SEG13_CHAR_RBRAC   = (SEG13_A|_______|_______|SEG13_D|_______|_______|_______|_______|_______|SEG13_J|SEG13_K|SEG13_M|_______)  # }
SEG13_CHAR_TILDE   = (_______|_______|SEG13_C|_______|_______|SEG13_F|SEG13_G|_______|_______|_______|_______|SEG13_M|_______)  # ~
SEG13_CHAR_DEL     = (_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______|_______)  # (del)
SEG13_CHAR_DP = (SEG13_DP)  # :
SEG13_CHAR_BLK = (SEG13_BLK)  # 无显

# ASCII chracters table
# Starts with SPACE
SEG13_Char_Code = [
    SEG13_CHAR_SP,     # (space)
    SEG13_CHAR_EXCLA,  # !
    SEG13_CHAR_DOUBL,  # "
    SEG13_CHAR_NUMBE,  # #
    SEG13_CHAR_DOLLA,  # $
    SEG13_CHAR_PERCE,  # %
    SEG13_CHAR_AMPER,  # &
    SEG13_CHAR_SINGL,  # '
    SEG13_CHAR_LEFTP,  # (
    SEG13_CHAR_RIGHP,  # )
    SEG13_CHAR_ASTER,  # *
    SEG13_CHAR_PLUS,   # +
    SEG13_CHAR_COMMA,  # ,
    SEG13_CHAR_DASH,   # -
    SEG13_CHAR_DOT,    # .
    SEG13_CHAR_FSLAS,  # /
    SEG13_CHAR_0,      # 0
    SEG13_CHAR_1,      # 1
    SEG13_CHAR_2,      # 2
    SEG13_CHAR_3,      # 3
    SEG13_CHAR_4,      # 4
    SEG13_CHAR_5,      # 5
    SEG13_CHAR_6,      # 6
    SEG13_CHAR_7,      # 7
    SEG13_CHAR_8,      # 8
    SEG13_CHAR_9,      # 9
    SEG13_CHAR_COLON,  # :
    SEG13_CHAR_SEMIC,  # ;
    SEG13_CHAR_LESST,  # <
    SEG13_CHAR_EQUAL,  # =
    SEG13_CHAR_MORET,  # >
    SEG13_CHAR_QUEST,  # ?
    SEG13_CHAR_AT,     # @
    SEG13_CHAR_A,      # A
    SEG13_CHAR_B,      # B
    SEG13_CHAR_C,      # C
    SEG13_CHAR_D,      # D
    SEG13_CHAR_E,      # E
    SEG13_CHAR_F,      # F
    SEG13_CHAR_G,      # G
    SEG13_CHAR_H,      # H
    SEG13_CHAR_I,      # I
    SEG13_CHAR_J,      # J
    SEG13_CHAR_K,      # K
    SEG13_CHAR_L,      # L
    SEG13_CHAR_M,      # M
    SEG13_CHAR_N,      # N
    SEG13_CHAR_O,      # O
    SEG13_CHAR_P,      # P
    SEG13_CHAR_Q,      # Q
    SEG13_CHAR_R,      # R
    SEG13_CHAR_S,      # S
    SEG13_CHAR_T,      # T
    SEG13_CHAR_U,      # U
    SEG13_CHAR_V,      # V
    SEG13_CHAR_W,      # W
    SEG13_CHAR_X,      # X
    SEG13_CHAR_Y,      # Y
    SEG13_CHAR_Z,      # Z
    SEG13_CHAR_LOBRA,  # [
    SEG13_CHAR_BSLAS,  # \
    SEG13_CHAR_ROBRA,  # ]
    SEG13_CHAR_CARET,  # ^
    SEG13_CHAR_USCOR,  # _
    SEG13_CHAR_BQUOT,  # `
    SEG13_CHAR_a,      # a
    SEG13_CHAR_b,      # b
    SEG13_CHAR_c,      # c
    SEG13_CHAR_d,      # d
    SEG13_CHAR_e,      # e
    SEG13_CHAR_f,      # f
    SEG13_CHAR_g,      # g
    SEG13_CHAR_h,      # h
    SEG13_CHAR_i,      # i
    SEG13_CHAR_j,      # j
    SEG13_CHAR_k,      # k
    SEG13_CHAR_l,      # l
    SEG13_CHAR_m,      # m
    SEG13_CHAR_n,      # n
    SEG13_CHAR_o,      # o
    SEG13_CHAR_p,      # p
    SEG13_CHAR_q,      # q
    SEG13_CHAR_r,      # r
    SEG13_CHAR_s,      # s
    SEG13_CHAR_t,      # t
    SEG13_CHAR_u,      # u
    SEG13_CHAR_v,      # v
    SEG13_CHAR_w,      # w
    SEG13_CHAR_x,      # x
    SEG13_CHAR_y,      # y
    SEG13_CHAR_z,      # z
    SEG13_CHAR_LBRAC,  # {
    SEG13_CHAR_VERTI,  # |
    SEG13_CHAR_RBRAC,  # }
    SEG13_CHAR_TILDE,  # ~
    SEG13_CHAR_DEL,    # (del)
]
