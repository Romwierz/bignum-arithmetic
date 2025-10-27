#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define LOW(x) x & 0b0011
#define HIGH(x) (x & 0b1100) >> 2
#define ADD_2_2(x, y, z) do { \
    uint8_t _x = (x); \
    uint8_t _y = (y); \
    if (_x + _y > 0b11) carry = 1; \
    else carry = 0; z = _x + _y; \
    z = LOW(z); \
} while(0)
#define ADDC_2_2(x, y, z, carry) do { \
    uint8_t _x = (x); \
    uint8_t _y = (y); \
    z = _x + _y + carry; \
    if (_x + _y + carry > 0b11) carry = 1; \
    else carry = 0; \
    z = LOW(z); \
} while(0)

void test_macro() {
    printf("low 0b1100: %d\n", LOW(0b1100));
    printf("low 0b1110: %d\n", LOW(0b1110));
    printf("low 0b1101: %d\n", LOW(0b1101));
    printf("high 0b1100: %d\n", HIGH(0b1100));
    printf("high 0b1000: %d\n", HIGH(0b1000));
    printf("high 0b0100: %d\n", HIGH(0b0100));

    uint8_t z;
    uint8_t carry;
    ADD_2_2(3, 3, z);
    printf("add 0b11 + 0b11 = %d\n", z);
    ADDC_2_2(3, 3, z, carry);
    printf("add 0b11 + 0b11 = %d with carry = %d\n", z, carry);
    ADD_2_2(2, 1, z);
    printf("add 0b10 + 0b01 = %d\n", z);
    carry = 0;
    ADDC_2_2(1, 0, z, carry);
    printf("add 0b01 + 0b00 = %d with carry = %d\n", z, carry);
}

uint8_t mul2x2_4(uint8_t x, uint8_t y) {
    if (x > 0b11 || y > 0b11) {
        printf("Error: numbers too big!\n");
        exit(EXIT_FAILURE);
    }
    return x*y;
}

uint8_t mul4x4_8(uint8_t x, uint8_t y) {
    if (x > 0b1111 || y > 0b1111) {
        printf("Error: numbers too big!\n");
        exit(EXIT_FAILURE);
    }

    uint8_t x1 = 0, x0 = 0, y1 = 0, y0 = 0, z3 = 0, z2 = 0, z1 = 0, z0 = 0, carry = 0, product = 0;
    y0 = LOW(y);
    y1 = HIGH(y);
    x0 = LOW(x);
    x1 = HIGH(x);

    product = mul2x2_4(y0,x0);
    z0 = LOW(product);
    z1 = HIGH(product);

    product = mul2x2_4(y0,x1);
    ADD_2_2(z1, LOW(product), z1);
    ADDC_2_2(z2, HIGH(product), z2, carry);
    ADDC_2_2(z3, 0, z3, carry);

    product = mul2x2_4(y1,x0);
    ADD_2_2(z1, LOW(product), z1);
    ADDC_2_2(z2, HIGH(product), z2, carry);
    ADDC_2_2(z3, 0, z3, carry);

    product = mul2x2_4(y1,x1);
    ADD_2_2(z2, LOW(product), z2);
    ADDC_2_2(z3, HIGH(product), z3, carry);

    return (z3 << 6) + (z2 << 4) + (z1 << 2) + z0;
}

int main(int argc, char *argv[]) {
    // test_macro();
    uint8_t x = 0, y = 0;
    if (argv[1] != NULL)
        x = atoi(argv[1]);
    if (argv[2] != NULL)
        y = atoi(argv[2]);

    printf("%d * %d = %d\n", x, y, mul4x4_8(x, y));
    return 0;
}
