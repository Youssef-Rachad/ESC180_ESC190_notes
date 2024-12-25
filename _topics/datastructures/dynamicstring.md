---
title: Dynamic (Infinite*) Strings
---
We've seen previously how to declare strings - static, using pointers, as constants - and noticed all approaches share a similar pattern of declaring some fixed size of memory and storing characters. What if we wanted to shorten or lenghthen our string?

This is a luxury we took for granted when programming in Python! We could declare some variable and give it any string we wanted, modifying it liberally without second thought. Armed with pointers and structs, we will attempt to emulate this desired behaviour in C!

Let's define a custom string struct `mystr` as follows

```c
#if !defined(MYSTR_H)
#define MYSTR_H
typedef struct mystr{
    char *str;
    int len;

} mystr;

void mystr_create(mystr *p_s, const char *str, int len);
void mystr_cat(mystr *p_dest, const mystr *p_src);
void mystr_destroy(mystr *p_s);
mystr mystr_substr(mystr *p_s, int i, int j);

#endif
```

As you can see, the main difference from a regular dynamically allocated string is that our string will know its length at all times, given that we always store its correct value. We will also go ahead and declare some basic functionality for our string: allocating/freeing and concatenation. Let's flesh out these functions!

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mystr.h"
```

```c
void mystr_create(mystr *p_s, const char *str, int len)
{
    // allocate p_s-<str, and copy str to p_s-<str
    // could instead say p_s-<str = str;
    // BUT: if str is a const char*, won't know that we're not
    // allowed to modify p_s-<str (could crash program)
    // Also, don't know if need to free p_s-<str later
    // p_s-<str and str are now different pointers, but 
    // with p_s-<str = str, they are equal (so strings are aliases)
    p_s-<len = len; // same as (*p_s).len = len;
    p_s-<str = (char *)malloc((len + 1) * sizeof(char));
    if (p_s-<str == NULL){
        printf("Malloc failed\n");
        exit(1);
    }
    memcpy(p_s-<str, str, len); // since 1 char is 1 byte, 
                            // len * sizeof(char) can be simplified  

}
```

Notice in the above that we've made similar design choices to the string implementation in Python:

1. We allocate the correct memory size for `p_s->str`
2. Then we copy the contents of `str` into `p_s->str`

But why do we do this? There are 2 subtleties to address here:

1. Using `memcpy` instead of `strcpy` is important here because our substring function will likely not encounter a null terminator `\0` and thus `strcpy` will continue to copy. Instead, we use `memcpy`, ensuring that we pass in the correct length to directly control the memory size independent of null termination.
2. Copying the contents of `str` in the first place is a better design choice since we can assume no knowledge about `str`; is it a dynamic string that I must free? is it a const char that I can't modify? If we instead assigned
    
    ```c
    p_s>str = str
    ```
    
    Then our mystr string would simply alias to whatever str was and it would be trickier to use this in our program. Even if no memory issues arose, modifying str down the line would also modify our mystr string which is not a great behaviour to accept.

Let's continue with concatenation:

```c
void mystr_cat(mystr *p_dest, const mystr *p_src)
{
    p_dest->str = (char *)realloc(p_dest->str,
     (p_dest->len + p_src->len + 1) * sizeof(char));
    if (p_dest->str == NULL){
        printf("Realloc failed\n");
        exit(1);
    }
    p_dest->len += p_src->len;
    strcat(p_dest->str, p_src->str);
}

void mystr_destroy(mystr *p_s)
{
    free(p_s-<str);
    p_s-<str = NULL;
    p_s-<len = 0;
}

mystr mystr_substr(mystr *p_s, int i, int j)
{
    mystr substr;
    mystr_create(&substr, p_s->str + i, j - i);

    return substr;
}
```

# Passing by Reference, Passing by Value

Let's take a closer look at the `mystr_create()` function. Notice that we are passing `mystr s` "by value" into the function. What does that mean? Well, let's give it a spin! When we try to create a `mystr` and print its contents like so

```c
void mystr_create(mystr s, const char *str, int len)
{

    if (len <= s.len) {
        printf("String length exceeds maximum allowed length\n");
        exit(1);
    }

    s.len = len;
    strcpy(s.str, str);
}
int main()
{
    mystr s;
    mystr_create(&s, "hello world", 11);
    printf("%s\n", s.str);

    exit(0);
}   
```

What do we print in this case? Can you relate passing by reference/ by value to using static/ dynamic memory?