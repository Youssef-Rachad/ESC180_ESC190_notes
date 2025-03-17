---
title: PyInteger
layout: default
jax: True
---
While in C the allowed integer datatypes (mainly `int`and `unsigned int`) have a restricted size, Python ==implements== a seemingly infinite integer. We will call this the `pyinteger` ADT and derive a possible implementation (such a task appeared on a past midterm!). The ADT `pyinteger` allows us to represent arbitrarily large integers and perform the two basic operations,

- Adding an integer to the `pyint`
- Adding 2 `pyint`s together

We first set up our header file, `pyinteger.h`:

```c
#if !defined(PYINT_H) // We want to define PyIntegers exactly once
#define PYINT_H
typedef struct pyint{
    int *buffer;
    int length;
} pyint;

void create_pyint(pyint *p, int length);
void destroy_pyint(pyint *p);
void set_pyint(pyint *p, int value);
void print_pyint(pyint *p);

void add_pyints(pyint *p, pyint *q);        // Add 2 pyints together
void add_pyint_scalar(pyint *p, int value); // Add an integer to a pyint

#endif
```

where `pyint` is a struct that contains the following fields:

- `buffer` is a pointer to an array of integers that stores the digits of the integer
- `length` is the number of digits in the integer

Here, we are representing an integer via an array where each element in this array is a digit from 0-9. For example, the integer 1234 would be represented as `[1, 2, 3, 4]`. Note that we will handle cases where the number we want to store exceeds the number of digits currently allocated in the buffer (and will typically double the array to avoid having to reallicate memory too often).

## Creating the Struct

Now we work in `pyint.c` and we wish to implement the ADT. But first, we can create a function that allows us to create a `pyint` struct which initially stores `int n`. What are some natural tasks that we must do?

- How can we determine the initial `length`? In other words, how do we make sure we initially allocated enough space for our array?
- How can we put the digits into the array `*buffer`? To do this, we need to find a good way of extracting the digits from the initial integer.

To determine the initial capacity, we need to determine the number of digits `int n` has.

I claim that the formula for the number of digits of 𝑛 is given bynum of digits=floor(log10⁡(𝑛))+1.

_Proof:_ A 𝑘-digit number can be written as𝑛=𝑎𝑘−110𝑘−1+𝑎𝑘−210𝑘−2+⋯+𝑎1101+𝑎.where the leading coefficient 𝑎𝑘−1≠0. To double-check this, note that 15=1×101+5 so the leading power is 𝑘−1. Note that:$10𝑘−1\le 𝑛<10𝑘$.It is important that the right inequality is strict! This is because 10𝑘 has 𝑘+1 digits while 𝑛 only has 𝑘 digits. For those who want more rigour, note that each 𝑎𝑖 is smaller or equal to 9 so we can bound 𝑛≤∑𝑖=0𝑘−19⋅10𝑖.  
  
Since the logarithm is a monotonically increasing function, we havelog10⁡(10𝑘−1)≤log10⁡(𝑛)<log10⁡(10𝑘)or equivalently,𝑘−1≤log10⁡(𝑛)<𝑘.Therefore, floor(log10⁡(𝑛))=𝑘−1 so𝑘=floor(log10⁡(𝑛))+1as expected.  
  
**However:** If 𝑛=0 then we get something that is undefined, so we have to treat this case separately.

Obviously, you are not expected to prove this on the midterm, but I provided the proof here for those who are interested and for the rigour. It's a handy fact to know though, so you don't need to be stressed about weird edge cases! The process of extracting the digits from the integer is a bit tricky, but it's something that we've done before! To get the last digit, we can compute𝑛%10.To get the second to last digit, we can shift all the digits by diving the number by 10 and ignoring the decimal part. Then we can repeatedly apply this same algorithm until we have no more digits left. Therefore, we should start from the end of the array and work our way backwards. Here is the code:

```C
void create_integer(pyinteger **pyint, int n){
    // Allocate memory for the pyinteger struct
    *pyint = (pyinteger*)malloc(sizeof(pyinteger));

    // Proven in a theorem
    if (n == 0){
        (*pyint)->capacity = 1;
    }
    else{
        (*pyint)->capacity = (int)(log10(n)) + 1;
    }

    // Currently the number of digits is the same as the capacity
    (*pyint)->num_digits = (*pyint)->capacity;

    // Allocate memory for the digits
    (*pyint)->digits = (int*)malloc(sizeof(int) * (*pyint)->capacity);

    // Fill the digits
    for (int loc = (*pyint)->num_digits - 1; loc >= 0; loc--){
        (*pyint)->digits[loc] = n % 10;
        n /= 10;
    }
}
```

## Implementing PlusPlus

Now we need to implement the function `plusplus`. This function should add `1` to the integer. Why might this be a tricky task? Well, the naive approach is to just add `1` to the units digit, but if the units digit is 9, then something weird might happen. Let's break it up into two cases, and work with the easier case first (this is a good idea in a test situation, since you know there will definitely be partial marks)

- Case 1: The units digit is not 9. We simply get the value at index `pyint->num_digits - 1` and check if it's a 9. If not, then we increment it by 1!
- Case 2: We draw analogy from long addition. We change the 9 into a 0, then carry over to the previous digit. If that digit is not 9, we add 1. If it is 9, we change it into a 0 and continue.

we can implement it (with a small hiccup we'll discuss in a bit) as follows:

```c
void plusplus(pyinteger *pyint){
    int loc;
    for (loc = pyint->num_digits - 1; loc >= 0; loc--){
        if (pyint->digits[loc] == 9){
            pyint->digits[loc] = 0;
        } else {
            pyint->digits[loc]++;
            break;
        }
    }
}
```

Note that at this stage, there is one more hiccup. If everything is 9, then the size of the number can increase! This specific case is a bit annoying, but just doing everything up to this point will give you 8/10 points. _If you can't fully figure how to solve a question, solving it partially can still land you a lot of points!_  
  
So how do we fix this? To deal with this case, we ask the following natural questions:

- How can we even detect if we need to do this case?
- How do we decide if we need to re-allocate memory?
- How do I shift the digits? (This is actually a bit misleading, as we'll see in a bit)

To detect if we even need to consider this case, there are many ways to do so. One way is to check the value of `loc` after the for loop finishes. If the for loop exits via the break statement, we should have `loc >= 0.` If it doesn't exit via the break statement, that means the first digit was also a 9, so `loc == 0.`  
  
How can we check if we need to re-allocate memory? At this point, we know that the number of digits has increased by 1, so we can update `num_digits.` Now we can check if the number of digits is greater than the capacity. If it is, then we need to re-allocate memory. We can do this by doubling the capacity.  
  
Finally, we need to be able to shift all the digits over. At least, this was my first thought when I saw the problem. However, if we work through a simple example (or think about it), at this point, every single digit should be 0! Therefore, all we need to do here is set the first digit to 1. Easy!

```c
void plusplus(pyinteger *pyint){
    int loc;
    for (loc = pyint->num_digits - 1; loc >= 0; loc--){
        if (pyint->digits[loc] == 9){
            pyint->digits[loc] = 0;
        } else {
            pyint->digits[loc]++;
            break;
        }
    }

    if(loc == -1){
        pyint->num_digits++;
        if(pyint->num_digits > pyint->capacity){
            pyint->capacity *= 2;
            // Reallocate memory for the digits
            pyint->digits = (int*)realloc(pyint->digits, sizeof(int) * pyint->capacity);
        }

        // First digit is 1
        pyint->digits[0] = 1;

        // Last digit is 0
        pyint->digits[pyint->num_digits - 1] = 0;
    }
}
```

## Implementing Add

Now we need to implement adding. First, why might this be a hard task? It's because the digits are not aligned in a "nice" manner. When we learn long addition in elementary school, we align the rightmost digit (ones digit) of the two numbers. But the way we implemented it here, we align the leftmost digit.  
  
Note: we did not get to finish this in class, but here are some ideas for solutions

- Partial Solution: You can call `plusplus()` multiple times. This is very easy to implement, since all you have to figure out is how to implement a for loop that adds 1 to `n1` a total of `n2` times.  
      
    One way to do this is to create a helper function to compare two pyintegers. Then we can create a temporary `pyinteger` and initialize it to 0. We then increment both this temporary pyinteger and `n1` until the temporary pyinteger is equal to `n2`.  
      
    This is not optimal, since the time complexity is 𝑂(𝑛log⁡𝑛) while the optimal complexity is 𝑂(log⁡𝑛). Because we care about time complexity in this course, you will not receive full marks, but it's possible to receive 8/10 points.
- Another way to solve this is to get rid of the annoying problem. Modify the `pyintegers` such that the units digit align. This can be done by shifting the digits over and filling everything before the leading digit with 0s. Then we can apply the standard long addition algorithm we learned in elementary school. Just remember to shift the digits back after we're done!
- Another way uses the same idea as above, but instead of shifting the digits, we can reformulate the standard "long addition" algorithm with indices, to make it easier to implement with code. Then all we have to do is write the algorithm with the C language!
