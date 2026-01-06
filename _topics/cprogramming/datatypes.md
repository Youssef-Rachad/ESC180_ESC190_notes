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
| double * | Address of a double variable |
| char * | Address of a char variable |

The last 3 types are known as **pointers** and are covered in more depth in a future [topic]({{ site.baseurl }}{% link _topics/cprogramming/pointers.md %}).
Note that we also haven't addressed strings (or lists for that matter); these a discussed in the [arrays and strings]({{ site.baseurl }}{% link _topics/cprogramming/arrays.md %}) topic.

# Brief note on `sizeof`
sizeof returns the size occupied in memory by the contents of a variable.
It returns a value of type `size_t`. The `size_t` is defined in a way to guarantee that it can count the elements in an array (among other use cases) so it is forced to be the size of the largest unsigned integer. On my machine, this means that it resembles the unsigned long long which is 64-bit in size. Note that the compiler will give a warning rather than an error when type casting a `size_t` to fit an integer in the limit that the size obtained does not exceed 32 bits (about 4 billion; nothing to worry about hopefully).

# How big is an integer?
Most computers nowadays use a 64 bit architecture but this was not always the case! Even before the standardisation of the 32-bit architecture, different computer platforms had different architectures. Note that an architecture size refers to the maximum register size available. 
In C, primitive type were introduces in part to abstract away the need to manually account for a specific platforms architecture and this concept is still applicable nowadays although you should be able to find the same primitive type sizes as shown in the following section.

| Primitive Type    | Size    |
| ----------------- | ------- |
| character (ASCII) | 1 byte  |
| integer           | 4 bytes |
| double            | 8 bytes |
| float             | 4 bytes |
| pointer           | 8 bytes |
| short integer     | 2 bytes |
| long integer      | 4 bytes |
| long long integer | 8 bytes |
| long double       | 8 bytes |
| size_t            | 8 bytes |
| boolean           | 1 byte  |

`unsigned` variants of datatypes are of the same length but have different possible values. Note that floats and doubles cannot be unsigned and that there are no long long doubles or long floats nor short short integers. The boolean type `bool` is available for the C99 standard onwards and takes on values of either `true` or `false`.

# Literals in C
A literal is a value that is used in the program, but not explicitly defined as a variable. 
Integers and decimal points are of int and double type, respectively. Symbols in single quotes are of char type, and strings (in double quotes) are of `const char *` type; which are discussed more in the
<a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/strings.html">arrays and strings </a>topic.

For example, we can break down a simple command like so
```C
int variable = 10;
```
- `int` is the data type
- `variable` is the variable name
- `10` is the literal (here, we can call it an integer literal)

Another example is when we write
```C
printf("Hello World!");
```
Here, we directly 'created' and passed `"Hello World"` into the `printf()` function.
This leads us to the first of many observations about how strings are implemented in C...

# Silly Strings
In the above example, we directly passed 
```c
printf("Hello World!");
```
In reality (or as we say: <b>at compile time</b>; which refers to the compiler processing the source code), the program is understood by the compiler more like
```cpp
char *str = "Hello World";
printf("%s", str);
```
In fact, `printf(const char *str)` is defined to take a pointer to a string as a first argument (the reason you can then use many arguments to specify the string formatting is because C implements varargs but these won't be covered).

Taking a second look at `char *str = "Hello World";`, we can learn more features of (static) C strings. Firstly, the notations
- `char *str`
- `char* str`
- `char * str`

are all valid, though we will prefer the first one by convention in this course.

Secondly, `str` only holds the address to `'H'`! So how then do we get all of the literal?
It turns out that strings are actually terminated by a <i>null terminator</i> represented by `\0`. This symbol tells the compiler that the string is done so when we pass the string literal "Hello World" what happens at compile time
1. A static string is instantiated in the memory `'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '\0'`
2. The address of 'H' is stored in a `char *` variable
3. That `char *` variable is passed to `printf()`
4. `printf()` goes to the address of 'H' and keeps reading the memory until it encounters the null terminator
5. "Hello World" is printed (there are more details here, starting with allocating a buffer to the standard output and so on but these details are not covered in the course)

Strings present interesting challenges, especially since we much of the nice abstractions we had by trading Python for C, and are further discussed in the <a href="{{ site.url }}{{ site.baseurl }}/topics/cprogramming/strings.html">strings </a>topic.

# Binary Numbers
A binary number is a number represented in its base 2 notation. We can interpret it as a sum of powers of 2 where the position of a digit determines its exponent. 

_small note: the convention in the notes is to write binary numbers in little endian meaning the least significant bit (LSB), so the smallest power of 2, is on the left. You DO NOT need to study this for ESC190._

For example, the number $$14_{10}$$ is written $$1110_2$$ in binary and we can represent it as $$1110_{2} = 1\cdot2^3+1\cdot2^2+1\cdot2^1+0\cdot2^0.$$
Recall this is exactly how we decompose numbers in decimal $$14=1\cdot10^1+4\cdot10^0.$$

Let's take a look now at how we might convert between $$14_{10}$$ and `$$1110_2$$.

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
1. $$2^0=1$$ doesn't fit in 0 so $$b_0=0$$. We are now done and have: $$14 = 2^3+2^2+2^1 = 1110_2.$$

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

Unicode is an interesting case where backwards compatability with ASCII was a must-requirement. To achieve this, Unicode uses the non-extended ASCII standard which only requires 7 bits then sets the first bit to 0 for a total of 8 bits (or 1 byte). None of the UTF encodings have a 0 as the first bit so this signals to Unicode readers that the character is an ASCII 1 byte character while ASCII readers are non the wiser since the bit string matches the standard.
