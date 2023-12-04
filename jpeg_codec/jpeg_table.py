import numpy as np

table_luminance_quantization = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68,109,103, 77],
    [24, 35, 55, 64, 81,104,113, 92],
    [49, 64, 78, 97,103,121,120,101],
    [72, 92, 95, 98,112,100,103, 99],
])

table_chrominance_quantization = np.array([
    [17, 18, 24, 47, 99, 99, 99, 99],
    [18, 21, 26, 66, 99, 99, 99, 99],
    [24, 26, 56, 99, 99, 99, 99, 99],
    [47, 66, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 99],
])

# Category length, Code word
tbl_luminance_dc = [
    [0,  2, 0b00],
    [1,  3, 0b010],
    [2,  3, 0b011],
    [3,  3, 0b100],
    [4,  3, 0b101],
    [5,  3, 0b110],
    [6,  4, 0b1110],
    [7,  5, 0b11110],
    [8,  6, 0b111110],
    [9,  7, 0b1111110],
    [10, 8, 0b11111110],
    [11, 9, 0b111111110],
]

# Category length, Code word
tbl_chrominance_dc = [
    [ 0,  2, 0b00],
    [ 1,  2, 0b01],
    [ 2,  2, 0b10],
    [ 3,  3, 0b110],
    [ 4,  4, 0b1110],
    [ 5,  5, 0b11110],
    [ 6,  6, 0b111110],
    [ 7,  7, 0b1111110],
    [ 8,  8, 0b11111110],
    [ 9,  9, 0b111111110],
    [10, 10, 0b1111111110],
    [11, 11, 0b11111111110],
]

# Run/Size, Code length, Code word
tbl_luminance_ac = [
    [0x0, 0x0,  4, 0b1010], # EOB
    [0x0, 0x1,  2, 0b00],
    [0x0, 0x2,  2, 0b01],
    [0x0, 0x3,  3, 0b100],
    [0x0, 0x4,  4, 0b1011],
    [0x0, 0x5,  5, 0b11010],
    [0x0, 0x6,  7, 0b1111000],
    [0x0, 0x7,  8, 0b11111000],
    [0x0, 0x8, 10, 0b1111110110],
    [0x0, 0x9, 16, 0b1111111110000010],
    [0x0, 0xA, 16, 0b1111111110000011],
    [0x1, 0x1,  4, 0b1100],
    [0x1, 0x2,  5, 0b11011],
    [0x1, 0x3,  7, 0b1111001],
    [0x1, 0x4,  9, 0b111110110],
    [0x1, 0x5, 11, 0b11111110110],
    [0x1, 0x6, 16, 0b1111111110000100],
    [0x1, 0x7, 16, 0b1111111110000101],
    [0x1, 0x8, 16, 0b1111111110000110],
    [0x1, 0x9, 16, 0b1111111110000111],
    [0x1, 0xA, 16, 0b1111111110001000],
    [0x2, 0x1,  5, 0b11100],
    [0x2, 0x2,  8, 0b11111001],
    [0x2, 0x3, 10, 0b1111110111],
    [0x2, 0x4, 12, 0b111111110100],
    [0x2, 0x5, 16, 0b1111111110001001],
    [0x2, 0x6, 16, 0b1111111110001010],
    [0x2, 0x7, 16, 0b1111111110001011],
    [0x2, 0x8, 16, 0b1111111110001100],
    [0x2, 0x9, 16, 0b1111111110001101],
    [0x2, 0xA, 16, 0b1111111110001110],
    [0x3, 0x1,  6, 0b111010],
    [0x3, 0x2,  9, 0b111110111],
    [0x3, 0x3, 12, 0b111111110101],
    [0x3, 0x4, 16, 0b1111111110001111],
    [0x3, 0x5, 16, 0b1111111110010000],
    [0x3, 0x6, 16, 0b1111111110010001],
    [0x3, 0x7, 16, 0b1111111110010010],
    [0x3, 0x8, 16, 0b1111111110010011],
    [0x3, 0x9, 16, 0b1111111110010100],
    [0x3, 0xA, 16, 0b1111111110010101],
    [0x4, 0x1,  6, 0b111011],
    [0x4, 0x2, 10, 0b1111111000],
    [0x4, 0x3, 16, 0b1111111110010110],
    [0x4, 0x4, 16, 0b1111111110010111],
    [0x4, 0x5, 16, 0b1111111110011000],
    [0x4, 0x6, 16, 0b1111111110011001],
    [0x4, 0x7, 16, 0b1111111110011010],
    [0x4, 0x8, 16, 0b1111111110011011],
    [0x4, 0x9, 16, 0b1111111110011100],
    [0x4, 0xA, 16, 0b1111111110011101],
    [0x5, 0x1,  7, 0b1111010],
    [0x5, 0x2, 11, 0b11111110111],
    [0x5, 0x3, 16, 0b1111111110011110],
    [0x5, 0x4, 16, 0b1111111110011111],
    [0x5, 0x5, 16, 0b1111111110100000],
    [0x5, 0x6, 16, 0b1111111110100001],
    [0x5, 0x7, 16, 0b1111111110100010],
    [0x5, 0x8, 16, 0b1111111110100011],
    [0x5, 0x9, 16, 0b1111111110100100],
    [0x5, 0xA, 16, 0b1111111110100101],
    [0x6, 0x1,  7, 0b1111011],
    [0x6, 0x2, 12, 0b111111110110],
    [0x6, 0x3, 16, 0b1111111110100110],
    [0x6, 0x4, 16, 0b1111111110100111],
    [0x6, 0x5, 16, 0b1111111110101000],
    [0x6, 0x6, 16, 0b1111111110101001],
    [0x6, 0x7, 16, 0b1111111110101010],
    [0x6, 0x8, 16, 0b1111111110101011],
    [0x6, 0x9, 16, 0b1111111110101100],
    [0x6, 0xA, 16, 0b1111111110101101],
    [0x7, 0x1,  8, 0b11111010],
    [0x7, 0x2, 12, 0b111111110111],
    [0x7, 0x3, 16, 0b1111111110101110],
    [0x7, 0x4, 16, 0b1111111110101111],
    [0x7, 0x5, 16, 0b1111111110110000],
    [0x7, 0x6, 16, 0b1111111110110001],
    [0x7, 0x7, 16, 0b1111111110110010],
    [0x7, 0x8, 16, 0b1111111110110011],
    [0x7, 0x9, 16, 0b1111111110110100],
    [0x7, 0xA, 16, 0b1111111110110101],
    [0x8, 0x1,  9, 0b111111000],
    [0x8, 0x2, 15, 0b111111111000000],
    [0x8, 0x3, 16, 0b1111111110110110],
    [0x8, 0x4, 16, 0b1111111110110111],
    [0x8, 0x5, 16, 0b1111111110111000],
    [0x8, 0x6, 16, 0b1111111110111001],
    [0x8, 0x7, 16, 0b1111111110111010],
    [0x8, 0x8, 16, 0b1111111110111011],
    [0x8, 0x9, 16, 0b1111111110111100],
    [0x8, 0xA, 16, 0b1111111110111101],
    [0x9, 0x1,  9, 0b111111001],
    [0x9, 0x2, 16, 0b1111111110111110],
    [0x9, 0x3, 16, 0b1111111110111111],
    [0x9, 0x4, 16, 0b1111111111000000],
    [0x9, 0x5, 16, 0b1111111111000001],
    [0x9, 0x6, 16, 0b1111111111000010],
    [0x9, 0x7, 16, 0b1111111111000011],
    [0x9, 0x8, 16, 0b1111111111000100],
    [0x9, 0x9, 16, 0b1111111111000101],
    [0x9, 0xA, 16, 0b1111111111000110],
    [0xA, 0x1,  9, 0b111111010],
    [0xA, 0x2, 16, 0b1111111111000111],
    [0xA, 0x3, 16, 0b1111111111001000],
    [0xA, 0x4, 16, 0b1111111111001001],
    [0xA, 0x5, 16, 0b1111111111001010],
    [0xA, 0x6, 16, 0b1111111111001011],
    [0xA, 0x7, 16, 0b1111111111001100],
    [0xA, 0x8, 16, 0b1111111111001101],
    [0xA, 0x9, 16, 0b1111111111001110],
    [0xA, 0xA, 16, 0b1111111111001111],
    [0xB, 0x1, 10, 0b1111111001],
    [0xB, 0x2, 16, 0b1111111111010000],
    [0xB, 0x3, 16, 0b1111111111010001],
    [0xB, 0x4, 16, 0b1111111111010010],
    [0xB, 0x5, 16, 0b1111111111010011],
    [0xB, 0x6, 16, 0b1111111111010100],
    [0xB, 0x7, 16, 0b1111111111010101],
    [0xB, 0x8, 16, 0b1111111111010110],
    [0xB, 0x9, 16, 0b1111111111010111],
    [0xB, 0xA, 16, 0b1111111111011000],
    [0xC, 0x1, 10, 0b1111111010],
    [0xC, 0x2, 16, 0b1111111111011001],
    [0xC, 0x3, 16, 0b1111111111011010],
    [0xC, 0x4, 16, 0b1111111111011011],
    [0xC, 0x5, 16, 0b1111111111011100],
    [0xC, 0x6, 16, 0b1111111111011101],
    [0xC, 0x7, 16, 0b1111111111011110],
    [0xC, 0x8, 16, 0b1111111111011111],
    [0xC, 0x9, 16, 0b1111111111100000],
    [0xC, 0xA, 16, 0b1111111111100001],
    [0xD, 0x1, 11, 0b11111111000],
    [0xD, 0x2, 16, 0b1111111111100010],
    [0xD, 0x3, 16, 0b1111111111100011],
    [0xD, 0x4, 16, 0b1111111111100100],
    [0xD, 0x5, 16, 0b1111111111100101],
    [0xD, 0x6, 16, 0b1111111111100110],
    [0xD, 0x7, 16, 0b1111111111100111],
    [0xD, 0x8, 16, 0b1111111111101000],
    [0xD, 0x9, 16, 0b1111111111101001],
    [0xD, 0xA, 16, 0b1111111111101010],
    [0xE, 0x1, 16, 0b1111111111101011],
    [0xE, 0x2, 16, 0b1111111111101100],
    [0xE, 0x3, 16, 0b1111111111101101],
    [0xE, 0x4, 16, 0b1111111111101110],
    [0xE, 0x5, 16, 0b1111111111101111],
    [0xE, 0x6, 16, 0b1111111111110000],
    [0xE, 0x7, 16, 0b1111111111110001],
    [0xE, 0x8, 16, 0b1111111111110010],
    [0xE, 0x9, 16, 0b1111111111110011],
    [0xE, 0xA, 16, 0b1111111111110100],
    [0xF, 0x0, 11, 0b11111111001],   # ZRL
    [0xF, 0x1, 16, 0b1111111111110101],
    [0xF, 0x2, 16, 0b1111111111110110],
    [0xF, 0x3, 16, 0b1111111111110111],
    [0xF, 0x4, 16, 0b1111111111111000],
    [0xF, 0x5, 16, 0b1111111111111001],
    [0xF, 0x6, 16, 0b1111111111111010],
    [0xF, 0x7, 16, 0b1111111111111011],
    [0xF, 0x8, 16, 0b1111111111111100],
    [0xF, 0x9, 16, 0b1111111111111101],
    [0xF, 0xA, 16, 0b1111111111111110],
]

# Run/Size, Code length, Code word
tbl_chrominance_ac =[
    [0x0, 0x0,  2, 0b00], # EOB
    [0x0, 0x1,  2, 0b01],
    [0x0, 0x2,  3, 0b100],
    [0x0, 0x3,  4, 0b1010],
    [0x0, 0x4,  5, 0b11000],
    [0x0, 0x5,  5, 0b11001],
    [0x0, 0x6,  6, 0b111000],
    [0x0, 0x7,  7, 0b1111000],
    [0x0, 0x8,  9, 0b111110100],
    [0x0, 0x9, 10, 0b1111110110],
    [0x0, 0xA, 12, 0b111111110100],
    [0x1, 0x1,  4, 0b1011],
    [0x1, 0x2,  6, 0b111001],
    [0x1, 0x3,  8, 0b11110110],
    [0x1, 0x4,  9, 0b111110101],
    [0x1, 0x5, 11, 0b11111110110],
    [0x1, 0x6, 12, 0b111111110101],
    [0x1, 0x7, 16, 0b1111111110001000],
    [0x1, 0x8, 16, 0b1111111110001001],
    [0x1, 0x9, 16, 0b1111111110001010],
    [0x1, 0xA, 16, 0b1111111110001011],
    [0x2, 0x1,  5, 0b11010],
    [0x2, 0x2,  8, 0b11110111],
    [0x2, 0x3, 10, 0b1111110111],
    [0x2, 0x4, 12, 0b111111110110],
    [0x2, 0x5, 15, 0b111111111000010],
    [0x2, 0x6, 16, 0b1111111110001100],
    [0x2, 0x7, 16, 0b1111111110001101],
    [0x2, 0x8, 16, 0b1111111110001110],
    [0x2, 0x9, 16, 0b1111111110001111],
    [0x2, 0xA, 16, 0b1111111110010000],
    [0x3, 0x1,  5, 0b11011],
    [0x3, 0x2,  8, 0b11111000],
    [0x3, 0x3, 10, 0b1111111000],
    [0x3, 0x4, 12, 0b111111110111],
    [0x3, 0x5, 16, 0b1111111110010001],
    [0x3, 0x6, 16, 0b1111111110010010],
    [0x3, 0x7, 16, 0b1111111110010011],
    [0x3, 0x8, 16, 0b1111111110010100],
    [0x3, 0x9, 16, 0b1111111110010101],
    [0x3, 0xA, 16, 0b1111111110010110],
    [0x4, 0x1,  6, 0b111010],
    [0x4, 0x2,  9, 0b111110110],
    [0x4, 0x3, 16, 0b1111111110010111],
    [0x4, 0x4, 16, 0b1111111110011000],
    [0x4, 0x5, 16, 0b1111111110011001],
    [0x4, 0x6, 16, 0b1111111110011010],
    [0x4, 0x7, 16, 0b1111111110011011],
    [0x4, 0x8, 16, 0b1111111110011100],
    [0x4, 0x9, 16, 0b1111111110011101],
    [0x4, 0xA, 16, 0b1111111110011110],
    [0x5, 0x1,  6, 0b111011],
    [0x5, 0x2, 10, 0b1111111001],
    [0x5, 0x3, 16, 0b1111111110011111],
    [0x5, 0x4, 16, 0b1111111110100000],
    [0x5, 0x5, 16, 0b1111111110100001],
    [0x5, 0x6, 16, 0b1111111110100010],
    [0x5, 0x7, 16, 0b1111111110100011],
    [0x5, 0x8, 16, 0b1111111110100100],
    [0x5, 0x9, 16, 0b1111111110100101],
    [0x5, 0xA, 16, 0b1111111110100110],
    [0x6, 0x1,  7, 0b1111001],
    [0x6, 0x2, 11, 0b11111110111],
    [0x6, 0x3, 16, 0b1111111110100111],
    [0x6, 0x4, 16, 0b1111111110101000],
    [0x6, 0x5, 16, 0b1111111110101001],
    [0x6, 0x6, 16, 0b1111111110101010],
    [0x6, 0x7, 16, 0b1111111110101011],
    [0x6, 0x8, 16, 0b1111111110101100],
    [0x6, 0x9, 16, 0b1111111110101101],
    [0x6, 0xA, 16, 0b1111111110101110],
    [0x7, 0x1,  7, 0b1111010],
    [0x7, 0x2, 11, 0b11111111000],
    [0x7, 0x3, 16, 0b1111111110101111],
    [0x7, 0x4, 16, 0b1111111110110000],
    [0x7, 0x5, 16, 0b1111111110110001],
    [0x7, 0x6, 16, 0b1111111110110010],
    [0x7, 0x7, 16, 0b1111111110110011],
    [0x7, 0x8, 16, 0b1111111110110100],
    [0x7, 0x9, 16, 0b1111111110110101],
    [0x7, 0xA, 16, 0b1111111110110110],
    [0x8, 0x1,  8, 0b11111001],
    [0x8, 0x2, 16, 0b1111111110110111],
    [0x8, 0x3, 16, 0b1111111110111000],
    [0x8, 0x4, 16, 0b1111111110111001],
    [0x8, 0x5, 16, 0b1111111110111010],
    [0x8, 0x6, 16, 0b1111111110111011],
    [0x8, 0x7, 16, 0b1111111110111100],
    [0x8, 0x8, 16, 0b1111111110111101],
    [0x8, 0x9, 16, 0b1111111110111110],
    [0x8, 0xA, 16, 0b1111111110111111],
    [0x9, 0x1,  9, 0b111110111],
    [0x9, 0x2, 16, 0b1111111111000000],
    [0x9, 0x3, 16, 0b1111111111000001],
    [0x9, 0x4, 16, 0b1111111111000010],
    [0x9, 0x5, 16, 0b1111111111000011],
    [0x9, 0x6, 16, 0b1111111111000100],
    [0x9, 0x7, 16, 0b1111111111000101],
    [0x9, 0x8, 16, 0b1111111111000110],
    [0x9, 0x9, 16, 0b1111111111000111],
    [0x9, 0xA, 16, 0b1111111111001000],
    [0xA, 0x1,  9, 0b111111000],
    [0xA, 0x2, 16, 0b1111111111001001],
    [0xA, 0x3, 16, 0b1111111111001010],
    [0xA, 0x4, 16, 0b1111111111001011],
    [0xA, 0x5, 16, 0b1111111111001100],
    [0xA, 0x6, 16, 0b1111111111001101],
    [0xA, 0x7, 16, 0b1111111111001110],
    [0xA, 0x8, 16, 0b1111111111001111],
    [0xA, 0x9, 16, 0b1111111111010000],
    [0xA, 0xA, 16, 0b1111111111010001],
    [0xB, 0x1,  9, 0b111111001],
    [0xB, 0x2, 16, 0b1111111111010010],
    [0xB, 0x3, 16, 0b1111111111010011],
    [0xB, 0x4, 16, 0b1111111111010100],
    [0xB, 0x5, 16, 0b1111111111010101],
    [0xB, 0x6, 16, 0b1111111111010110],
    [0xB, 0x7, 16, 0b1111111111010111],
    [0xB, 0x8, 16, 0b1111111111011000],
    [0xB, 0x9, 16, 0b1111111111011001],
    [0xB, 0xA, 16, 0b1111111111011010],
    [0xC, 0x1,  9, 0b111111010],
    [0xC, 0x2, 16, 0b1111111111011011],
    [0xC, 0x3, 16, 0b1111111111011100],
    [0xC, 0x4, 16, 0b1111111111011101],
    [0xC, 0x5, 16, 0b1111111111011110],
    [0xC, 0x6, 16, 0b1111111111011111],
    [0xC, 0x7, 16, 0b1111111111100000],
    [0xC, 0x8, 16, 0b1111111111100001],
    [0xC, 0x9, 16, 0b1111111111100010],
    [0xC, 0xA, 16, 0b1111111111100011],
    [0xD, 0x1, 11, 0b11111111001],
    [0xD, 0x2, 16, 0b1111111111100100],
    [0xD, 0x3, 16, 0b1111111111100101],
    [0xD, 0x4, 16, 0b1111111111100110],
    [0xD, 0x5, 16, 0b1111111111100111],
    [0xD, 0x6, 16, 0b1111111111101000],
    [0xD, 0x7, 16, 0b1111111111101001],
    [0xD, 0x8, 16, 0b1111111111101010],
    [0xD, 0x9, 16, 0b1111111111101011],
    [0xD, 0xA, 16, 0b1111111111101100],
    [0xE, 0x1, 14, 0b11111111100000],
    [0xE, 0x2, 16, 0b1111111111101101],
    [0xE, 0x3, 16, 0b1111111111101110],
    [0xE, 0x4, 16, 0b1111111111101111],
    [0xE, 0x5, 16, 0b1111111111110000],
    [0xE, 0x6, 16, 0b1111111111110001],
    [0xE, 0x7, 16, 0b1111111111110010],
    [0xE, 0x8, 16, 0b1111111111110011],
    [0xE, 0x9, 16, 0b1111111111110100],
    [0xE, 0xA, 16, 0b1111111111110101],
    [0xF, 0x0, 10, 0b1111111010], # ZRL
    [0xF, 0x1, 15, 0b111111111000011],
    [0xF, 0x2, 16, 0b1111111111110110],
    [0xF, 0x3, 16, 0b1111111111110111],
    [0xF, 0x4, 16, 0b1111111111111000],
    [0xF, 0x5, 16, 0b1111111111111001],
    [0xF, 0x6, 16, 0b1111111111111010],
    [0xF, 0x7, 16, 0b1111111111111011],
    [0xF, 0x8, 16, 0b1111111111111100],
    [0xF, 0x9, 16, 0b1111111111111101],
    [0xF, 0xA, 16, 0b1111111111111110],
]


def make_mask(s, v):
    m = 2**s - 1
    s = 16-s
    m <<= s
    v <<= s
    return [v, m]

def add_mask(src):
    dst = []
    for v in src:
        dst.append(v + make_mask(v[-2], v[-1]))
    return dst

def conv_table_dc(src):
    tbl = [None for _ in range(12)]
    for s in src:
        tbl[s[0]] = {
#           'size': s[0],
            'length': s[1],
            'code': s[2],
            'value': s[3],
            'mask': s[4],
        }
    return tbl

def conv_table_ac(src):
    tbl = [[None for _ in range(11)] for _ in range(16)]
    for s in src:
        tbl[s[0]][s[1]] = {
#           'run': s[0],
#           'size': s[1],
            'length': s[2],
            'code': s[3],
            'value': s[4],
            'mask': s[5],
        }
    return tbl

list_luminance_dc = add_mask(tbl_luminance_dc)
list_chrominance_dc = add_mask(tbl_chrominance_dc)
list_luminance_ac = add_mask(tbl_luminance_ac)
list_chrominance_ac = add_mask(tbl_chrominance_ac)

table_luminance_dc = conv_table_dc(list_luminance_dc)
table_chrominance_dc = conv_table_dc(list_chrominance_dc)
table_luminance_ac = conv_table_ac(list_luminance_ac)
table_chrominance_ac = conv_table_ac(list_chrominance_ac)


# DCT hyoer-parameter
T = 8
K = 8     # 復元時にどれだけ解像度を良くするかを決定するパラメータ
channel = 3

# DCT weight
def dct_weight(x, y, u, v):
    cu = 1.0
    cv = 1.0
    if u == 0:
        cu /= np.sqrt(2)
    if v == 0:
        cv /= np.sqrt(2)
    theta = np.pi / (2 * T)
    return (( 2 * cu * cv / T) * np.cos((2*x+1)*u*theta) * np.cos((2*y+1)*v*theta))

# テーブル作成
table_dct = np.ndarray((8, 8, 8, 8))
table_idct = np.ndarray((8, 8, 8, 8))
for y in range(8):
    for x in range(8):
        for v in range(8):
            for u in range(8):
                table_dct[v, u, y, x] = dct_weight(x, y, u, v)
table_idct = table_dct.transpose(2, 3, 0, 1)


tbl_zigzag = [
    [ 0,  1,  5,  6, 14, 15, 27, 28],
    [ 2,  4,  7, 13, 16, 26, 29, 42],
    [ 3,  8, 12, 17, 25, 30, 41, 43],
    [ 9, 11, 18, 24, 31, 40, 44, 53],
    [10, 19, 23, 32, 39, 45, 52, 54],
    [20, 22, 33, 38, 46, 51, 55, 60],
    [21, 34, 37, 47, 50, 56, 59, 61],
    [35, 36, 48, 49, 57, 58, 62, 63],
]


def make_zigzag():
    a = []
    p = []
    for y in range(8):
        for x in range(8):
            a.append(tbl_zigzag[y][x])
            p.append((x, y))
    a = np.array(a)
    p = np.array(p)
    return p[np.argsort(a)]


table_zigzag = make_zigzag()