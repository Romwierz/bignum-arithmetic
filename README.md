## **Multiplication**

`R7_R6_R5_R4` x `R3_R2_R1_R0` = `X7_X6_X5_X4_X3_X2_X1_X0`

#### Step 1

```
a)
product = ro * r4
x0 = low(product)
x1 = high(product)

b)
product = ro * r5
x1 = x1 + low(product)
x2 = high(product) + C
x3 = C

c)
product = ro * r6
x2 = x2 + low(product)
x3 = x3 + high(product) + C
x4 = C

d)
product = ro * r7
x3 = x3 + low(product)
x4 = x4 + high(product) + C
x5 = C
```

#### Step 2

```
a)
product = r1 * r4
x1 = x1 + low(product)
x2 = x2 + high(product) + C
x3 = x3 + C
x4 = x4 + C
x5 = x5 + C
x6 = C

b)
product = r1 * r5
x2 = x2 + low(product)
x3 = x3 +high(product) + C
x4 = x4 + C
x5 = x5 + C
x6 = x6 + C
x7 = C

c)
product = r1 * r6
x3 = x3 + low(product)
x4 = x4 + high(product) + C
x4 = C

d)
product = r1 * r7
x3 = x3 + low(product)
x4 = x4 + high(product) + C
x5 = x5 + C
x6 = x6 + C
x7 = x7 + C
```

#### Step 3

```
a)
product = r2 * r4
x2 = x2 + low(product)
x3 = x3 + high(product) + C
x4 = x4 + C
x5 = x5 + C
x6 = x6 + C
x7 = x7 + C

b)
product = r2 * r5
x3 = x3 + low(product)
x4 = x4 + high(product) + C
x5 = x5 + C
x6 = x6 + C
x7 = x7 + C

c)
product = r2 * r6
x4 = x4 + low(product)
x5 = x5 + high(product) + C
x6 = x6 + C
x7 = x7 + C

d)
product = r2 * r7
x4 = x4 + low(product)
x5 = x5 + high(product) + C
x6 = x6 + C
x7 = x7 + C
```

#### Step 4

```
a)
product = r3 * r4
x3 = x3 + low(product)
x4 = x4 + high(product) + C
x5 = x5 + C
x6 = x6 + C
x7 = x7 + C

b)
product = r3 * r5
x4 = x4 + low(product)
x5 = x4 +high(product) + C
x6 = x6 + C
x7 = x7 + C

c)
product = r3 * r6
x5 = x5 + low(product)
x6 = x6 + high(product) + C
x7 = x7 + C

d)
product = r3 * r7
x6 = x6 + low(product)
x7 = x7 + high(product) + C
```
