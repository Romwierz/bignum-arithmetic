from .bignum import *
from .bignum import print_num

def test_add8():
    a = 255 
    b = 255 
    carry_in = 0

    (result, carry_out) = add8(a, b, carry_in)
    print(hex(a), "+", hex(b), "=", result, "with carry =", carry_out)

def test_mul8():
    a = 255
    b = 255

    (lo, hi) = mul8(a, b)
    print(hex(a), "*", hex(b), "=", "(hi)", hex(hi), "(lo)", hex(lo))

def test_add_bignum():
    # store big numbers as byte sequences from LSB to MSB
    a = [0xff, 0xff, 0xff, 0xff]
    b = [0x02, 0x00, 0x00, 0x00]

    print_num(a)
    print(" +", end=" ")
    print_num(b)
    print(" =", end=" ")

    (result, carry) = add_bignum(a, b)
    print_num(result)
    print(" with carry =", carry)

def test_sub_bignum():
    a = [0xfd, 0xff, 0xff, 0xff]
    b = [0x02, 0x00, 0x00, 0x00]
    b = [0xff, 0xff, 0xff, 0xff]

    print_num(a)
    print(" -", end=" ")
    print_num(b)
    print(" =", end=" ")

    (result, borrow) = sub_bignum(a, b)
    print_num(result)
    print(" with borrow =", borrow)

def test_mul_bignum():
    a = [0xff, 0xff]
    b = [0xff, 0xff]

    print_num(a)
    print(" *", end=" ")
    print_num(b)
    print(" =", end=" ")

    result = mul_bignum(a, b)
    print_num(result)
    print("")

def test_div_bignum():
    a = [0xff, 0xff]
    b = [0x01, 0x00]

    print_num(a)
    print(" /", end=" ")
    print_num(b)
    print(" =", end=" ")

    quotient, remainder = div_bignum(a, b)
    print_num(quotient)
    print(" with remainder =", end=" ")
    print_num(remainder)
    print("")

def main():
    print("Hello there!")

if __name__=="__main__":
    main()
    # test_add_bignum()
    # test_mul_bignum()
    test_sub_bignum()
    test_div_bignum()
    quit()
    a = 2
    b = 5
    m = 7
    n_bits = 3

    _a = montgomery_convert_in(a, m, n_bits)
    _b = montgomery_convert_in(b, m, n_bits)
    _x = mul_montgomery(_a, _b, m, n_bits)
    print(_x)
    montgomery_convert_out(_x, m, n_bits)


