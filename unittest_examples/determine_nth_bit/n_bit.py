# Is nth bit a 1 of a given byte?
def get_bit(byte, n):

    index = n - 1
    num = 2 ** index
    bit = byte & num
    return (bit!=0)