from python.utils import get_bits_cnt

def mul_montgomery(a, b, m):
    n_bits = get_bits_cnt(m)
    a_ = a
    result = 0
    for i in range(n_bits):
        if a & 1:
            result += b
        if result & 1:
            result += m
        result >>= 1
        a >>= 1
    if result >= m:
        result -= m

    return result

def montgomery_convert_in(x, m):
    n_bits = get_bits_cnt(m)
    R = 1 << n_bits
    return (x * R) % m

def montgomery_convert_out(x, m):
    # MontMul(x, 1)
    return mul_montgomery(x, 1, m)

