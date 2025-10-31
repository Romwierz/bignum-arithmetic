def print_num(num):
    print("0x", end="")
    for i in reversed(range(len(num))):
        if num[i] < 0x10:
            print("0", end="")
        print(format(num[i], 'x'), end="")

def add8(a, b, carry_in = 0):
    total = a + b + carry_in
    result = total & 0xFF
    carry_out = 1 if total > 0xFF else 0
    return result, carry_out

def mul8(a, b):
    product = a * b
    lo = product & 0xFF
    hi = (product >> 8) & 0xFF
    return lo, hi

def add_bignum(a, b):
    n = max(len(a), len(b))
    result = [0] * n
    carry = 0
    for i in range(n):
        result[i], carry = add8(a[i], b[i], carry)
    return result, carry

def mul_bignum(a, b):
    n = len(a)
    m = len(b)
    result = [0] * (n + m)
    for i in range(n):
        carry = 0
        for j in range(m):
            lo, hi = mul8(a[i], b[j])
            result[i + j], c = add8(result[i + j], lo, carry)
            # hi, carry = add8(hi, c)
            # result[i + j + 1] = add8(result[i + j + 1], hi)
            carry = hi + c
        result[i + m], _ = add8(result[i + m], carry)
    return result

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

def main():
    print("Hello there!")

if __name__=="__main__":
    main()
    # test_add_bignum()
    test_mul_bignum()

