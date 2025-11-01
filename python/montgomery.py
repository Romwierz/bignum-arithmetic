def mul_montgomery(a, b, m, n_bits):
    a_ = a
    result = 0
    # i = 0
    # while a > 0:
    #     print(i, end=": ")
    #     if a & 1:
    #         result += b
    #     if result & 1: # is odd
    #         result += m
    #     result = result >> 1
    #     print(result)
    #     a = a >> 1
    #     i += 1
    # if result >= m:
    #     result = result - m
    for i in range(n_bits):
        a = a >> i
        if (a) & 1:
            result += b
        if result & 1:
            result += m
        result >>= 1
    if result >= m:
        result -= m

    print(a_, end="")
    print(" *", end=" ")
    print(b, end="")
    print(" mod", end=" ")
    print(m, end="")
    print(" =", end=" ")
    print(result)
    return result

def montgomery_convert_in(x, m, n_bits):
    R = 1 << n_bits
    return (x * R) % m

def montgomery_convert_out(x, m, n_bits):
    # MontMul(x, 1)
    return mul_montgomery(x, 1, m, n_bits)

