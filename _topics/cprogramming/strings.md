---
title: Strings
layout: default
jax: True
---
# Strings
Strings in C can be a bit tricky at first because a lot of abstraction is not immediately built into the language. We will see how a string is derived from the primitive type `char` and we will implement some string functions while exploring the `<string.h>` where a standard implementation of most string operations is provided by the language.
# The `const char*` type
When we pass a string directly into a function, for example in `printf("I love ESC190");`, we don't think about the datatype of the string and often confuse it. In fact it is a `const char*` which means: 'a pointer to an array of characters which are constant'. 
This is more relevant in the following example
```c
int main()
{
  const char* course = "ESC190";
  return 0;
}
```
Here, `course` is a string in the sense that it is a pointer to an array of characters. The pointer points to location in memory but the contents of that contiguous block of memory cannot be changed, hence it is immutable.
The compiler gives an error whenever the contents are modified in any way.
```c
int main()
{
  const char* course = "ESC190";
  course = "ESC102";              // Error
  return 0;
}
```
Let's see other ways of declaring strings such that we can manipulate them more flexibly.
# Static Strings
By definition, a string is an array of characters so naturally we could declare a string as follows:
```c
int main()
{
  char course[] = {'P', 'R', 'A', 'X', 'I', 'S', '\0' };
  printf("My next lecture is %s", course); // we %s to format a string
}
```
Notice the trailing `\0` character called the terminator. We say that strings are null-terminated and this lets the compiler know how much memory the string occupies. 
In essence, accessing a string variable involves the compiler locating a character in memory and reading the adjacent character in order until the null-terminator tells it to stop reading.

Of course, we can use a shorthand called a string literal which comes with a built-in null-terminator
```c
int main()
{
  char course[] = "PRAXIS";
  printf("My last lecture was %s", course);
}
```
Notice that characters are enclosed in single quotes ( ' ) while strings are enclosed in double quotes ( " ). This syntax is enforced by the compiler. Since strings are arrays, we can access them similarly
```c
int main()
{
  char course[] = "PRAXIS"
  for(int idx = 0; i <= 7; i++) {
    printf("%c", course[idx]);   // The output will be:
                                 // P
                                 // R
                                 // A
                                 // X
                                 // I
                                 // S
                                 // \0
  }
}
```
# Dynamic Strings
We found that static strings are mutable, which is a nice feature for changing the actual content but still does not allow us to modify the length of the string. In fact, statically allocated memory cannot be resised in C. To overcome this, we dynamically allocate memory large enough to hold some characters and assign the first letter to a pointer:
```c
int main()
{
  char *mystr = (char *)malloc(20 * sizeof(char));
}
```

This allows us to construct a string with similar functionality to strings as defined in Python [DynamicString]({{ site.baseurl }}{% link _topics/datastructures/dynamicstring.md %})

# String Methods
The C language provides many common functions to manipulate strings in the `string.h` library (which you can read for yourself [here](https://gcc.gnu.org/git.html)). They implement good practices, make it easy to code with strings and since they often have implementations relevant to ESC190, we will try to implement them independently.

Note that, along with many standard functions in C that involve strings (and arrays as a good practice), the caller allocates the buffer instead of the callee. This means that it is best practice to create the destination string for `strcpy` inside the `main` function (or wherever `strcpy()` is called) instead of inside `strcpy` because allocating and freeing memory becomes clear and obvious.

# String method strcpy
We might know how long of a string we will need for our program but not necessarily what to populate it with. It can be tempting to write `char *name = "Alice";` but this way does not preserve mutability - for example, `name[0] = 'a';` later on leads to undefined behaviour and may crash our program.

The strings header defines a string copy method `strcpy` which we can use like so:
```c
#include <stdio.h>
#include <string.h>

int main()
{
  char *name[20];
  strcpy(name, "Alice"); // name = {'A', 'l', 'i', 'c', 'e', '\0'}
}
```
The function `strcpy()` is provided by the strings library `string.h` and is used ubiquitously to copy strings across buffers (buffers is a general term for memory blocks). We will look at an implementation of `strcpy` function. 

```c
char *my_strcpy(char *dest, const char *src)
{
  char *dest_ptr = dest; // store the destination pointer for return

  while(*src){ //equivalently: *str != '\0'
    *dest++ = *src++; // 1. Access the values at dest and src
                      // 2. Assign value of src to value of dest
                      // 3. Increment dest and src addresses
    // Another way to write this is
    // dest[0] = src[0]; assign the current value of src to dest
    // dest++;           advance dest pointer
    // src++ ;           advance src pointer 
  }
  
  // Eventually we reach the '\0' character which also needs to be copied to dest
  *dest = *src;

  // We saved the original pointer because the increment operator made the pointer point to "the rest of the string" and forgetting about the first character at each iteration 
  return dest_ptr;
}

int main()
{
  char my_class[] = "ESC190";
  char next_lec[100];
  my_strcpy(next_lec, my_class);

  printf("My next lecture is %s\n", next_lec); // "ESC190"
}
```

# strcat
Concatenating strings is more involved in C now that we are aware of memory management. While `strcat` makes this pain free, it's still valuable to understand the underlying idea behind the implementation. Recall that string functions rely on the caller to allocate correctly sized destination buffers. With that in mind, `strcat` expects the `dest` buffer to already contain some string as well as enough space to fit the `src` string. We can reach the end of `dest` (where a `'\0'` terminates the string) and copy over `src` in the remaining space using `strcpy`. Let's look at an implementation of the `strcat` function
```c
char *my_strcat(char *dest, const char *src){
  char *dest_ptr = dest; // store the destination pointer for return

  
  while(*dest){
    dest++;
  }
  // Equivalently we can write the above while-loop
  // while(*dest++); // 1. Access the value stored at str
                    // 2. Check that it is not NULL (or not equal to '\0')
                    // 3. Increment the value of str by +1
  // Again, this is not recommended in practice
  
  my_strcpy(dest, src);
  
  return dest_ptr;
}
```


