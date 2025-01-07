---
title: Data Types in C Overview
layout: default
jax: True
---
# Types in C
Variables in Python are dynamically typed, which means that it's the interpreter's job to infer what is the type of a variable when declaring/accessing it. 
We let go of this abstraction in C, where we must specificy the type of the data stored inside a variable. 

Below are some examples of types:

| Type | Example |
| ---- | ------- |
| int | Integer number |
| double  | Double-precision floating point number |
| char | ASCII character (the basic english character set) |
| int * | Address of an int variable |
| double * | Addres of a double variable |
| char * | Address of a char variable |

The last 3 types are known as **pointers** and are covered in more depth in a future [topic]({{ site.baseurl }}{% link _topics/cprogramming/pointers.md %}).
Note that we also haven't addressed strings (or lists for that matter); these a discussed in the [arrays and strings]({{ site.baseurl }}{% link _topics/cprogramming/arrays.md %}) topic.

# Literals in C
A literal is a value that is used in the program, but not explicitly defined as a variable. 
Integers and decimal points are of int and double type, respectively. Symbols in single quotes are of char type, and strings (in double quotes) are of const char * type; which are discussed in the arrays and strings topic.

# Binary Numbers
A binary number is a number represented in its base 2 notation. We can interpret it as a sum of powers of 2 where the position of a digit determines its exponent. 

_small note: the convention in the notes is to write binary numbers in little endian meaning the least significant bit (LSB), so the smallest power of 2, is on the left. You DO NOT need to study this for ESC190._

For example, the number `14_{10}` is written `1110_2` in binary and we can represent it as $$1110_{2} = 1\cdot2^3+1\cdot2^2+1\cdot2^1+0\cdot2^0.$$
Recall this is exactly how we decompose numbers in decimal $$14=1\cdot10^1+4\cdot10^0.$$

Let's take a look now at how we might convert between `14_{10}` and `1110_2`.

Going from right to left:
1. 14 is even, so the last binary digit is a 0. We now have to represent $$\frac{14-0}{2}=7$$.
1. 7 is odd, so the 2nd last binary digit is a 1. We now have to represent $$\frac{7-1}{2}=3$$.
1. 3 is odd, so the 3rd last binary digit is a 1. We now have to represent $$\frac{3-1}{2}=1$$.
1. 1 in binary is still 1 so the 4th last digit is a 1.

We thus write, from right to left: $$1110_{2}$$

This process can be done in Python too
```python
def get_decimal_digits(d):
  digits = []
  while d != 0:
    digits = [(d % 10)] + digits
    d //= 10
  return digits

def get_binary_digits(d):
  digits = []
  while d != 0:
    digits = [(d % 2)] + digits
    d //= 2
  return digits

print(get_binary_digits(14))
print(get_decimal_digits(521))
print(get_binary_digits(25))
```

Going from left to right:
- We want to write 14 as a sum of powers of 2, we do this by removing the largest power of 2 at each iteration until we are done. Thus the problem is to determine the coefficients such that $$14 = b_k2^k+b_{k-1}2^{k-1}+\dots+b_12+b_0$$
1. We determine that 14 is a 4 bit digit binary number.
1. The largest power of 2 that fits in 14 is 8 so $$b_3=1$$. We now need to represent $$14-8=6$$.
1. The largest power of 2 that fits in 6 is 4 so $$b_2=1$$. We now need to represent $$6-4=2$$.
1. The largest power of 2 that fits in 2 is exactly 2 so $$b_1=1$$. We now need to represent $$2-2=0$$.
1. $2^0=1$ doesn't fit in 0 so $$b_0=0$$. We are now done and have: $$14 = 2^3+2^2+2^1 = 1110_2.$$

**What about negative numbers? and floating point number?**
The numbers we dealt with above are called _unsigned_ because we assume they are positive when looking at their binary representation. However, dealing with negative numbers necessarily means using 1 bit of information to communicate whether the number is positive or negative (after all, binary is most useful in digital logic which is strictly a 2 state system of HIGH or LOW so its not practical to write a minus sign in hardware). 

In 8 bit binary representations (it's common to use 8 bits because they form a byte), it's common to use the bit of highest value as a sign bit where 0 means positive and 1 means negative. This leaves 7 bits to represent the decimal portion of the number. For example $$b_7b_6b_5b_4b_3b_2b_1b_0=\begin{cases}+b_6b_5b_4b_3b_2b_1b_0& \text{if } b_7 = 0\\ +b_6b_5b_4b_3b_2b_1b_0&\text{if }b_7=1\end{cases}$$

Note: you might notice that a naive approach would lead us to have 2 zeros (namely, 00000000 and 10000000), we avoid this redundancy in a system called two's complement where 10000000 actually rolls over to negative values, starting at -128.

| Unsigned Decimal | Two's Complement Decimal | Binary Representation |
| ---------------  | ---------------          | --------------------- |
| 0                | 0                        | 00000000              |
| 1                | 1                        | 00000001              |
| ...              | ...                      | ...                   |
| 127              | 127                      | 01111111              |
| 128              | -128                     | 10000000              |
| 129              | -127                     | 10000001              |
| ...              | ...                      | ...                   |
| 255              | -1                       | 11111111              |

There are many other schemes to represent numbers using binary and these are best done through codified standards, for example:
- IEEE754 defines how to interpret floating point numbers
- ASCII is the old American standard for text (but is easiest to teach since it uses 8 bit binary)
- Unicode is the modern standard for text and includes nearly all languistic characters and pictograms for art and emojis. 

Unicode is an interesting case where backwards compatability with ASCII was a must-requirement. To achieve this, Unicode uses the non-extended ASCII standard which only requires 7 bits then sets the first bit to 0 for a total of 8 bits. None of the UTF encodings have a 0 as the first bit so this signals to Unicode readers that the character is an ASCII 1 byte character while ASCII readers are non the wiser since the bit string matches the standard.
